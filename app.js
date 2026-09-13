(function () {
  const data = window.ADMISSIONS_DATA || [];
  const meta = window.ADMISSIONS_META || {};
  const facultyAll = window.FACULTY_DATA || [];
  const facultyMeta = window.FACULTY_META || {};

  const REGIONS = [
    { id: "all", label: "全部地区" },
    { id: "hk", label: "香港本地" },
    { id: "hk_mainland", label: "香港·大陆校区" },
    { id: "usa", label: "美国" },
    { id: "singapore", label: "新加坡" },
    { id: "japan", label: "日本" },
    { id: "korea", label: "韩国" },
    { id: "europe", label: "欧洲" },
  ];
  const DEGREES = [
    { id: "all", label: "全部学位" },
    { id: "phd", label: "PhD / 研究型" },
    { id: "master", label: "硕士（授课为主）" },
  ];
  const FUNDING = [
    { id: "all", label: "全部资助" },
    { id: "full", label: "通常全奖/带薪" },
    { id: "partial", label: "部分/竞争" },
    { id: "rare", label: "多为自费" },
  ];

  const state = {
    region: "all",
    degree: "phd",
    funding: "all",
    q: "",
    sort: "deadline",
    onlyHigh: false,
    onlyGraphics: false,
    selectedId: null,
  };

  const $ = (id) => document.getElementById(id);

  function fundingLabel(level) {
    if (level === "full") return "通常全奖";
    if (level === "partial") return "部分/竞争";
    if (level === "rare") return "多为自费";
    return level || "未知";
  }

  function parseDeadline(d) {
    if (!d) return "9999-99-99";
    const m = String(d).match(/(\d{4}-\d{2}-\d{2})/);
    return m ? m[1] : "9999-99-99";
  }

  function matchFaculty(schoolName) {
    const s = String(schoolName || "").toLowerCase();
    return facultyAll.filter((f) =>
      (f.schoolKeys || []).some((k) => s.includes(String(k).toLowerCase()))
    );
  }

  function schoolHasGraphicsFaculty(schoolName) {
    return matchFaculty(schoolName).some((f) => f.hasGraphics);
  }

  function filtered() {
    let rows = data.slice();
    if (state.region !== "all") rows = rows.filter((r) => r.region === state.region);
    if (state.degree !== "all") rows = rows.filter((r) => r.degree === state.degree);
    if (state.funding !== "all") rows = rows.filter((r) => r.fundingLevel === state.funding);
    if (state.onlyHigh) rows = rows.filter((r) => r.confidence === "high");
    if (state.onlyGraphics) rows = rows.filter((r) => schoolHasGraphicsFaculty(r.school));
    const q = state.q.trim().toLowerCase();
    if (q) {
      rows = rows.filter((r) => {
        const fac = matchFaculty(r.school);
        const facBlob = fac
          .map((f) =>
            [f.name, f.title, ...(f.interests || []).map((i) => i.text), f.notes].join(" ")
          )
          .join(" ");
        const blob = [
          r.school,
          r.program,
          r.campus,
          r.fields && r.fields.join(" "),
          r.notes,
          r.funding,
          r.portalName,
          facBlob,
        ]
          .join(" ")
          .toLowerCase();
        return blob.includes(q);
      });
    }
    const fundRank = { full: 0, partial: 1, rare: 2, unknown: 3 };
    rows.sort((a, b) => {
      if (state.sort === "school") return a.school.localeCompare(b.school);
      if (state.sort === "region")
        return (
          (a.regionLabel || "").localeCompare(b.regionLabel || "") ||
          a.school.localeCompare(b.school)
        );
      if (state.sort === "funding")
        return (
          (fundRank[a.fundingLevel] ?? 9) - (fundRank[b.fundingLevel] ?? 9) ||
          parseDeadline(a.deadline).localeCompare(parseDeadline(b.deadline))
        );
      return (
        parseDeadline(a.deadline).localeCompare(parseDeadline(b.deadline)) ||
        a.school.localeCompare(b.school)
      );
    });
    return rows;
  }

  function makePills(container, options, key) {
    container.innerHTML = "";
    options.forEach((opt) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "pill" + (state[key] === opt.id ? " active" : "");
      b.textContent = opt.label;
      b.addEventListener("click", () => {
        state[key] = opt.id;
        render();
      });
      container.appendChild(b);
    });
  }

  function renderStats(rows) {
    const all = data;
    const el = $("stats");
    const n = (pred) => all.filter(pred).length;
    el.innerHTML = [
      ["筛选结果", rows.length],
      ["总条目", all.length],
      ["导师库", facultyAll.length],
      ["图形学导师", facultyMeta.graphicsCount || facultyAll.filter((f) => f.hasGraphics).length],
      ["香港本地", n((r) => r.region === "hk")],
      ["美国", n((r) => r.region === "usa")],
      ["欧洲", n((r) => r.region === "europe")],
    ]
      .map(([k, v]) => `<div class="stat"><b>${v}</b><span>${k}</span></div>`)
      .join("");
  }

  function renderList(rows) {
    const pane = $("listPane");
    if (!rows.length) {
      pane.innerHTML = '<div class="count-bar">无匹配结果</div>';
      return;
    }
    if (!state.selectedId || !rows.find((r) => r.id === state.selectedId)) {
      state.selectedId = rows[0].id;
    }
    pane.innerHTML =
      `<div class="count-bar">显示 ${rows.length} 条 · 点击查看详情与导师</div>` +
      rows
        .map((r) => {
          const active = r.id === state.selectedId ? " active" : "";
          const gfx = schoolHasGraphicsFaculty(r.school);
          const nFac = matchFaculty(r.school).length;
          return `<article class="item${active}" data-id="${r.id}">
            <div class="item-top"><h3>${escapeHtml(r.school)}</h3><span class="badge">${escapeHtml(r.deadline || "—")}</span></div>
            <div class="meta">${escapeHtml(r.regionLabel)} · ${escapeHtml(r.campus || "")}</div>
            <div class="meta">${escapeHtml(r.program)}</div>
            <div class="badges">
              <span class="badge ${r.degree}">${r.degree === "phd" ? "PhD" : "硕士"}</span>
              <span class="badge ${r.fundingLevel}">${fundingLabel(r.fundingLevel)}</span>
              <span class="badge ${r.region === "usa" ? "usa" : r.region.startsWith("hk") ? "hk" : ""}">${escapeHtml(r.regionLabel)}</span>
              ${gfx ? '<span class="badge gfx">图形学导师</span>' : ""}
              ${nFac ? `<span class="badge">导师 ${nFac}</span>` : '<span class="badge">导师待补</span>'}
              ${r.confidence === "high" ? '<span class="badge">高置信</span>' : '<span class="badge">需核对</span>'}
            </div>
          </article>`;
        })
        .join("");

    pane.querySelectorAll(".item").forEach((el) => {
      el.addEventListener("click", () => {
        state.selectedId = el.getAttribute("data-id");
        render();
      });
    });
  }

  function renderFacultyHtml(schoolName) {
    const list = matchFaculty(schoolName);
    if (!list.length) {
      return `<div class="faculty-block">
        <h3>相关导师 / 实验室</h3>
        <p class="faculty-hint">本库暂未收录该校详细导师名单。请到院系 People / Research 页面查找；图形学可搜 Computer Graphics / Rendering / Geometry。</p>
      </div>`;
    }
    const cards = list
      .map((f) => {
        const interests = (f.interests || [])
          .map((it) => {
            const t = escapeHtml(it.text);
            return it.graphics
              ? `<li><span class="gfx">${t}</span></li>`
              : `<li>${t}</li>`;
          })
          .join("");
        const rec = f.recruiting
          ? '<span class="recruiting-tag">在招/欢迎套磁</span>'
          : "";
        return `<div class="faculty-card${f.hasGraphics ? " gfx-card" : ""}">
          <h4>${escapeHtml(f.name)}${rec}</h4>
          <p class="role">${escapeHtml(f.title || "")}</p>
          <ul class="interests">${interests}</ul>
          ${f.notes ? `<p class="notes">${escapeHtml(f.notes)}</p>` : ""}
          <p style="margin:8px 0 0"><a class="home" href="${escapeAttr(f.homepage)}" target="_blank" rel="noopener">个人主页 / 实验室</a></p>
        </div>`;
      })
      .join("");
    return `<div class="faculty-block">
      <h3>相关导师 / 实验室（${list.length}）</h3>
      <p class="faculty-hint">${escapeHtml(facultyMeta.note || "")} <strong>加粗高亮</strong> = 图形学相关方向。</p>
      <div class="faculty-grid">${cards}</div>
    </div>`;
  }

  function renderDetail(rows) {
    const pane = $("detailPane");
    const r = rows.find((x) => x.id === state.selectedId);
    if (!r) {
      pane.innerHTML = '<div class="empty">← 选择左侧条目查看详情</div>';
      return;
    }
    pane.innerHTML = `
      <h2>${escapeHtml(r.school)}</h2>
      <p class="sub">${escapeHtml(r.program)} · QS CS 参考 ${escapeHtml(String(r.qsCs2026))} · 置信度 ${escapeHtml(r.confidence)}</p>
      <div class="badges" style="margin-bottom:14px">
        <span class="badge ${r.degree}">${r.degree === "phd" ? "PhD/研究型" : "硕士"}</span>
        <span class="badge">${escapeHtml(r.regionLabel)}</span>
        <span class="badge ${r.fundingLevel}">${fundingLabel(r.fundingLevel)}</span>
        <span class="badge">${escapeHtml((r.fields || []).join(" / "))}</span>
        ${schoolHasGraphicsFaculty(r.school) ? '<span class="badge gfx">含图形学导师</span>' : ""}
      </div>
      <div class="grid2">
        <div class="kv"><h4>申请 / 入学时间</h4><p><b>截止：</b>${escapeHtml(r.deadline)}<br/><b>入学：</b>${escapeHtml(r.intake)}<br/>${escapeHtml(r.deadlineDetail || "")}</p></div>
        <div class="kv"><h4>有关 Funding</h4><p>${escapeHtml(r.funding)}</p></div>
        <div class="kv"><h4>招生要求</h4><p>${escapeHtml(r.requirements)}</p></div>
        <div class="kv"><h4>语言要求</h4><p>${escapeHtml(r.english)}</p></div>
        <div class="kv"><h4>注册 / 申请网站</h4><p><b>${escapeHtml(r.portalName)}</b><br/><a href="${escapeAttr(r.applyUrl)}" target="_blank" rel="noopener">${escapeHtml(r.applyUrl)}</a></p></div>
        <div class="kv"><h4>校区 / 备注</h4><p>${escapeHtml(r.campus || "")}<br/>${escapeHtml(r.notes || "")}<br/><span style="color:#9aabbd">来源：${escapeHtml(r.source || "")}</span></p></div>
      </div>
      ${renderFacultyHtml(r.school)}
      <div class="actions">
        <a class="btn" href="${escapeAttr(r.applyUrl)}" target="_blank" rel="noopener">打开官方申请页</a>
        <button type="button" class="btn ghost" id="copyLink">复制链接</button>
      </div>
    `;
    const copyBtn = document.getElementById("copyLink");
    if (copyBtn) {
      copyBtn.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(r.applyUrl);
          copyBtn.textContent = "已复制";
          setTimeout(() => (copyBtn.textContent = "复制链接"), 1200);
        } catch (_) {
          copyBtn.textContent = "复制失败";
        }
      });
    }
  }

  function escapeHtml(s) {
    return String(s ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  function escapeAttr(s) {
    return String(s ?? "").replace(/"/g, "&quot;");
  }

  function exportCsv(rows) {
    const headers = [
      "regionLabel",
      "degree",
      "school",
      "campus",
      "program",
      "deadline",
      "intake",
      "fundingLevel",
      "funding",
      "english",
      "requirements",
      "applyUrl",
      "confidence",
      "facultyNames",
      "graphicsFaculty",
    ];
    const lines = [headers.join(",")].concat(
      rows.map((r) => {
        const fac = matchFaculty(r.school);
        const row = {
          ...r,
          facultyNames: fac.map((f) => f.name).join("; "),
          graphicsFaculty: fac
            .filter((f) => f.hasGraphics)
            .map((f) => f.name)
            .join("; "),
        };
        return headers
          .map((h) => {
            const v = String(row[h] ?? "").replace(/"/g, '""');
            return `"${v}"`;
          })
          .join(",");
      })
    );
    const blob = new Blob(["\ufeff" + lines.join("\n")], {
      type: "text/csv;charset=utf-8",
    });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "phd-2027-filtered.csv";
    a.click();
    URL.revokeObjectURL(a.href);
  }

  function render() {
    makePills($("degreePills"), DEGREES, "degree");
    makePills($("regionPills"), REGIONS, "region");
    makePills($("fundingPills"), FUNDING, "funding");
    const rows = filtered();
    renderStats(rows);
    renderList(rows);
    renderDetail(rows);
  }

  $("metaLine").textContent = `${meta.scope || ""} · 共 ${meta.count || data.length} 条 · 导师 ${facultyAll.length} · 生成 ${meta.generated || ""}`;
  $("disclaimer").textContent =
    (meta.disclaimer || "") +
    " " +
    (facultyMeta.note || "");

  $("q").placeholder = "学校 / 导师 / graphics / rendering / HKPFS…";

  $("q").addEventListener("input", (e) => {
    state.q = e.target.value;
    render();
  });
  $("sort").addEventListener("change", (e) => {
    state.sort = e.target.value;
    render();
  });
  $("onlyHigh").addEventListener("change", (e) => {
    state.onlyHigh = e.target.checked;
    render();
  });
  $("onlyGraphics").addEventListener("change", (e) => {
    state.onlyGraphics = e.target.checked;
    render();
  });
  $("btnReset").addEventListener("click", () => {
    state.region = "all";
    state.degree = "phd";
    state.funding = "all";
    state.q = "";
    state.sort = "deadline";
    state.onlyHigh = false;
    state.onlyGraphics = false;
    $("q").value = "";
    $("sort").value = "deadline";
    $("onlyHigh").checked = false;
    $("onlyGraphics").checked = false;
    render();
  });
  $("btnExport").addEventListener("click", () => exportCsv(filtered()));

  render();
})();
