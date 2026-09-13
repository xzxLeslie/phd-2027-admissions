# -*- coding: utf-8 -*-
"""Generate faculty.js — professors linked to schools in admissions UI."""
from pathlib import Path
import json

out = Path(__file__).resolve().parent

# schoolKeys: substrings matched against admissions record.school (case-insensitive)
# graphics=True => whole person prioritized; interests with isGraphics get <strong>
faculty = []


def F(school_keys, name, title, homepage, interests, notes="", recruiting=None):
    """interests: list of {text, graphics: bool} or plain strings (auto-detect)."""
    norm = []
    for it in interests:
        if isinstance(it, dict):
            norm.append(it)
        else:
            g = any(
                k in it.lower()
                for k in [
                    "graphic",
                    "render",
                    "geometry",
                    "animation",
                    "simulation",
                    "visualization",
                    "visual computing",
                    "3d ",
                    "3d-",
                    "nerf",
                    "gaussian",
                    "splatting",
                    "digital human",
                    "character",
                    "mesh",
                    "cad",
                    "fabrication",
                    "vr",
                    "ar",
                    "xr",
                    "hci",
                    "sketch",
                    "appearance",
                    "shading",
                    "ray tracing",
                    "physically-based",
                    "physical simulation",
                    "computational imaging",
                    "computational photography",
                    "image synthesis",
                ]
            )
            # Don't mark pure CV/ML without 3D/graphics cues as graphics unless keyword hits
            if it.lower() in ("hci",) or "hci" in it.lower() and "graphic" not in it.lower():
                # HCI alone: only graphics if coupled — keep auto
                pass
            norm.append({"text": it, "graphics": g})
    has_g = any(x.get("graphics") for x in norm)
    faculty.append(
        {
            "schoolKeys": school_keys,
            "name": name,
            "title": title,
            "homepage": homepage,
            "interests": norm,
            "hasGraphics": has_g,
            "notes": notes,
            "recruiting": recruiting,
        }
    )


# ========== HONG KONG ==========
F(
    ["university of hong kong", "(hku)"],
    "Taku Komura",
    "Professor, Computing & Data Science",
    "https://i.cs.hku.hk/~taku/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Character Animation", "graphics": True},
        {"text": "Physical Simulation", "graphics": True},
        {"text": "3D Modelling", "graphics": True},
        "Embodied AI / Robotics",
    ],
    notes="CGVU Lab; actively recruiting PhD/MPhil/RA",
    recruiting=True,
)
F(
    ["university of hong kong", "(hku)"],
    "Yizhou Yu",
    "Professor (Visual Computing / AI)",
    "https://i.cs.hku.hk/~yzyu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Computer Vision",
        "Deep Learning",
        {"text": "Visual Computing", "graphics": True},
    ],
)

F(
    ["chinese university of hong kong (cuhk)", "cuhk)", "the chinese university of hong kong"],
    "Chi-Wing Fu (Philip)",
    "Professor, CSE",
    "https://www.cse.cuhk.edu.hk/~cwfu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Computational Design", "graphics": True},
        {"text": "3D Generation / Editing", "graphics": True},
        "Computer Vision",
        "HCI",
    ],
    notes="Looking for PhD students in computational design / graphics",
    recruiting=True,
)
F(
    ["chinese university of hong kong (cuhk)", "the chinese university of hong kong"],
    "Pheng-Ann Heng",
    "Professor, CSE",
    "https://www.cse.cuhk.edu.hk/~pheng/",
    [
        {"text": "Visualization", "graphics": True},
        {"text": "VR / Medical Graphics", "graphics": True},
        "Medical Imaging AI",
    ],
)

F(
    ["hkust (clear water bay)", "hong kong university of science"],
    "Hongbo Fu",
    "Professor, CSE / Arts & Machine Creativity",
    "https://hongbofu.people.ust.hk/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Sketching / Creative AI", "graphics": True},
        "HCI",
        "Computer Vision",
    ],
    notes="Also joint with HKUST(GZ) CMA",
    recruiting=True,
)
F(
    ["hkust (clear water bay)", "hong kong university of science"],
    "Pedro Sander",
    "Professor, CSE",
    "https://cse.hkust.edu.hk/~psander/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Real-time Rendering", "graphics": True},
        {"text": "Geometry Processing", "graphics": True},
        {"text": "GPU / Graphics Hardware", "graphics": True},
    ],
)
F(
    ["hkust (clear water bay)"],
    "Chi-Keung Tang",
    "Professor, CSE",
    "https://cse.hkust.edu.hk/~cktang/",
    [
        "Computer Vision",
        {"text": "Computer Graphics", "graphics": True},
        "Machine Learning",
    ],
)
F(
    ["hkust (clear water bay)"],
    "Chiew-Lan Tai",
    "Professor, CSE",
    "https://cse.hkust.edu.hk/~taicl/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Geometric Modeling", "graphics": True},
        "HCI",
    ],
)
F(
    ["hkust (clear water bay)"],
    "Long Quan",
    "Professor, CSE",
    "https://cse.hkust.edu.hk/~quan/",
    ["3D Computer Vision", {"text": "3D Reconstruction", "graphics": True}, "SLAM"],
)

F(
    ["city university of hong kong", "cityuhk"],
    "Jing Liao",
    "Associate Professor (Creative Media / Graphics-related)",
    "https://liaojing.github.io/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Image / Video Synthesis", "graphics": True},
        "Generative AI",
    ],
)
F(
    ["hong kong polytechnic", "polyu)"],
    "Ping Li",
    "Associate Professor (Comp)",
    "https://www.comp.polyu.edu.hk/~p.li/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
        "Multimedia",
    ],
)

# HK mainland
F(
    ["hkust (guangzhou)"],
    "Hongbo Fu",
    "Professor (joint CMA)",
    "https://hongbofu.people.ust.hk/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Creative AI / Sketch", "graphics": True},
        "HCI",
    ],
    notes="Joint appointment HKUST Clear Water Bay + GZ",
)
F(
    ["hkust (guangzhou)"],
    "Zeyu Wang",
    "Assistant Professor, CIS Lab",
    "https://cislab.hkust-gz.edu.cn/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "HCI / XR",
        {"text": "Generative Content Creation", "graphics": True},
    ],
    recruiting=True,
)
F(
    ["hkust (guangzhou)"],
    "Yan Li",
    "Assistant Professor, Embodied Spatial AI",
    "https://yanyan-li.github.io/",
    [
        {"text": "Gaussian Splatting SLAM", "graphics": True},
        {"text": "3D/4D Reconstruction", "graphics": True},
        "Embodied AI",
        "Robotics",
    ],
    notes="PhD openings Spring/Fall 2027",
    recruiting=True,
)
F(
    ["cuhk-shenzhen", "cuhk, shenzhen"],
    "Jia Kui / Gorilla Lab (group)",
    "Professor / Lab (geometry & 3D AI)",
    "https://www.cuhk.edu.cn/en",
    [
        {"text": "3D Generative AI", "graphics": True},
        "Computer Vision",
        "Machine Learning",
    ],
    notes="Confirm current PI pages on SSE / data science school sites",
)

# ========== SINGAPORE ==========
F(
    ["national university of singapore", "(nus)"],
    "Kok-Lim Low",
    "Senior Lecturer, SoC",
    "https://www.comp.nus.edu.sg/~lowkl/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Real-time Rendering", "graphics": True},
        {"text": "Computational Art / Aesthetics", "graphics": True},
    ],
)
F(
    ["national university of singapore", "(nus)"],
    "Tan Tiow Seng",
    "Associate Professor, SoC",
    "https://www.comp.nus.edu.sg/cs/people/tants/",
    [
        {"text": "Geometric Algorithms for Graphics", "graphics": True},
        {"text": "Interactive Graphics / Visualization", "graphics": True},
        "GPU Geometry",
    ],
)
F(
    ["national university of singapore"],
    "Angela Yao",
    "Associate Professor (Vision)",
    "https://www.comp.nus.edu.sg/~yaoa/",
    ["Computer Vision", "Human Motion", "Video Understanding"],
)
F(
    ["nanyang technological university", "(ntu)"],
    "Ying He",
    "Associate Professor, CCDS",
    "https://personal.ntu.edu.sg/yhe/index.html",
    [
        {"text": "Geometry Processing", "graphics": True},
        {"text": "Geometric Modeling", "graphics": True},
        {"text": "3D Vision / 3D Deep Learning", "graphics": True},
    ],
)
F(
    ["nanyang technological university", "(ntu)"],
    "Alexei Sourin",
    "Associate Professor, CCDS",
    "https://www3.ntu.edu.sg/home/ASSourin/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Virtual Reality", "graphics": True},
        "Visualization",
        "HCI",
    ],
)
F(
    ["sutd"],
    "Sai-Kit Yeung",
    "Associate Professor (typical graphics/vision faculty — verify)",
    "https://www.sutd.edu.sg/",
    [
        {"text": "3D Computer Vision", "graphics": True},
        {"text": "Computational Design", "graphics": True},
    ],
    notes="Confirm current affiliation on SUTD directory",
)

# ========== JAPAN ==========
F(
    ["university of tokyo"],
    "Takeo Igarashi",
    "Professor (typical; verify lab page)",
    "https://www-ui.is.s.u-tokyo.ac.jp/~takeo/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "HCI",
        {"text": "Interactive Design", "graphics": True},
    ],
)
F(
    ["institute of science tokyo", "science tokyo"],
    "Science Tokyo Graphics / Vision faculty",
    "See ISCT directories",
    "https://www.isct.ac.jp/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Computer Vision",
        "Imaging",
    ],
    notes="原Tokyo Tech 图形/视觉组；请按学院目录套磁",
)
F(
    ["oist"],
    "OIST faculty (interdisciplinary)",
    "PhD program (rotation)",
    "https://www.oist.jp/admissions",
    ["Computational neuroscience", "AI", "Imaging"],
    notes="OIST 不先绑单一导师；入学后轮转",
)

# ========== KOREA ==========
F(
    ["kaist"],
    "KAIST Visual Computing / Graphics groups",
    "See School of Computing",
    "https://cs.kaist.ac.kr/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Computer Vision",
        "HCI",
    ],
    notes="在 cs.kaist.ac.kr People 中筛选 Graphics 标签导师",
)
F(
    ["seoul national university", "(snu)"],
    "SNU Computer Graphics Lab faculty",
    "CSE / ECE",
    "https://cse.snu.ac.kr/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["postech"],
    "POSTECH Computer Graphics Lab",
    "CSE",
    "https://www.postech.ac.kr/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Rendering / Geometry", "graphics": True},
    ],
)

# ========== USA (major graphics schools) ==========
F(
    ["massachusetts institute of technology"],
    "Frédo Durand",
    "Professor, EECS / CSAIL",
    "https://people.csail.mit.edu/fredo/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Rendering / Computational Photography", "graphics": True},
        {"text": "Differentiable Rendering", "graphics": True},
    ],
)
F(
    ["massachusetts institute of technology"],
    "Wojciech Matusik",
    "Professor, EECS / CSAIL",
    "https://www.csail.mit.edu/person/wojciech-matusik",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Computational Fabrication", "graphics": True},
        {"text": "Digital Humans", "graphics": True},
    ],
)
F(
    ["massachusetts institute of technology"],
    "Justin Solomon",
    "Associate Professor, EECS",
    "https://people.csail.mit.edu/jsolomon/",
    [
        {"text": "Geometry Processing", "graphics": True},
        {"text": "Geometric Machine Learning", "graphics": True},
    ],
)

F(
    ["stanford university"],
    "Kayvon Fatahalian",
    "Associate Professor, CS",
    "http://graphics.stanford.edu/~kayvonf/",
    [
        {"text": "Visual Computing Systems", "graphics": True},
        {"text": "Interactive Graphics", "graphics": True},
        "ML Systems",
    ],
)
F(
    ["stanford university"],
    "Doug James",
    "Professor, CS",
    "http://graphics.stanford.edu/~djames/",
    [
        {"text": "Physics-based Animation", "graphics": True},
        {"text": "Computer Graphics", "graphics": True},
        "Sound / Simulation",
    ],
)
F(
    ["stanford university"],
    "C. Karen Liu",
    "Professor, CS",
    "https://profiles.stanford.edu/c-karen-liu",
    [
        {"text": "Character Animation", "graphics": True},
        {"text": "Physics-based Graphics", "graphics": True},
        "Robotics",
    ],
)
F(
    ["stanford university"],
    "Jiajun Wu",
    "Assistant Professor, CS",
    "https://jiajunwu.com/",
    [
        {"text": "3D Computer Vision / Graphics", "graphics": True},
        {"text": "Neural Scene Representations", "graphics": True},
        "AI",
    ],
)
F(
    ["stanford university"],
    "Gordon Wetzstein",
    "Associate Professor, EE (by courtesy CS)",
    "https://stanford.edu/~gordonwz/",
    [
        {"text": "Neural Rendering", "graphics": True},
        {"text": "Computational Imaging / Displays", "graphics": True},
        "AI + Optics",
    ],
)
F(
    ["stanford university"],
    "Maneesh Agrawala",
    "Professor, CS",
    "https://graphics.stanford.edu/~maneesh/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "HCI",
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["stanford university"],
    "Leonidas Guibas",
    "Professor, CS",
    "https://geometry.stanford.edu/member/guibas/",
    [
        {"text": "Geometry Processing", "graphics": True},
        {"text": "3D Shape Analysis", "graphics": True},
        "Geometric ML",
    ],
)

F(
    ["carnegie mellon"],
    "CMU Graphics Lab faculty (e.g. Keenan Crane, Ioannis Gkioulekas, …)",
    "SCS / RI",
    "https://www.cs.cmu.edu/~graphics/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Geometry / Rendering / Imaging", "graphics": True},
    ],
    notes="见 CMU Graphics 主页完整名单",
)
F(
    ["uc berkeley"],
    "Berkeley Graphics / Visual Computing faculty",
    "EECS",
    "https://www2.eecs.berkeley.edu/Research/Areas/GR/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Computational Imaging", "graphics": True},
        "Vision",
    ],
)
F(
    ["university of washington"],
    "Steve Seitz / UW Graphics & Imaging Lab",
    "Professor, CSE",
    "https://www.cs.washington.edu/research/graphics/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "3D Computer Vision", "graphics": True},
        {"text": "Image-based Rendering", "graphics": True},
    ],
)
F(
    ["georgia tech", "georgia institute"],
    "Greg Turk",
    "Professor, Interactive Computing",
    "https://www.cc.gatech.edu/~turk/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Geometry / Animation", "graphics": True},
    ],
)
F(
    ["georgia tech"],
    "Bo Zhu",
    "Associate Professor",
    "https://faculty.cc.gatech.edu/~bozhu/",
    [
        {"text": "Physics Simulation", "graphics": True},
        {"text": "Computer Graphics", "graphics": True},
        "Scientific ML / Generative AI",
    ],
)
F(
    ["uc san diego"],
    "Tzu-Mao Li",
    "Assistant Professor, CSE",
    "https://cseweb.ucsd.edu/~tzli/",
    [
        {"text": "Differentiable Rendering", "graphics": True},
        {"text": "Computer Graphics", "graphics": True},
        "Visual Computing",
    ],
    recruiting=True,
)
F(
    ["cornell university"],
    "Cornell Graphics / Vision faculty",
    "CS",
    "https://www.cs.cornell.edu/research/graphics/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Rendering / Perception", "graphics": True},
    ],
)
F(
    ["princeton university"],
    "Princeton Graphics / Vision",
    "CS",
    "https://www.cs.princeton.edu/research/areas",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["california institute of technology", "caltech"],
    "Caltech Computing + Math Sciences / EE imaging",
    "CMS / EE",
    "https://www.cms.caltech.edu/",
    [
        {"text": "Computational Imaging", "graphics": True},
        "Vision",
    ],
)
F(
    ["harvard university"],
    "Harvard SEAS Visual Computing",
    "SEAS",
    "https://www.seas.harvard.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision / HCI",
    ],
)
F(
    ["ucla"],
    "UCLA Computer Graphics & Vision faculty",
    "CS",
    "https://www.cs.ucla.edu/research/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["uiuc", "university of illinois"],
    "UIUC Graphics group",
    "CS",
    "https://cs.illinois.edu/research/areas/graphics-and-visualization",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["university of michigan"],
    "Michigan Computer Graphics / Interactive Systems",
    "CSE",
    "https://cse.engin.umich.edu/research/computer-graphics/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "HCI",
    ],
)
F(
    ["ut austin", "university of texas"],
    "UT Austin Graphics / Vision",
    "CS",
    "https://www.cs.utexas.edu/research/areas",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["columbia university"],
    "Columbia Computer Graphics Group",
    "CS",
    "https://www.cs.columbia.edu/graphics/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Appearance / Rendering", "graphics": True},
    ],
)
F(
    ["university of pennsylvania", "upenn"],
    "Penn GRASP / Graphics-related",
    "CIS",
    "https://www.cis.upenn.edu/research/",
    [
        {"text": "3D Vision / Robotics Graphics", "graphics": True},
        "Perception",
    ],
)
F(
    ["university of southern california", "usc)"],
    "USC ICT / Graphics Lab",
    "CS",
    "https://www.cs.usc.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Digital Humans / Animation", "graphics": True},
    ],
)
F(
    ["new york university", "nyu)"],
    "NYU Courant Media / Graphics",
    "CS",
    "https://cs.nyu.edu/home/research/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["johns hopkins"],
    "JHU Vision & Graphics",
    "CS",
    "https://www.cs.jhu.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["yale university"],
    "Yale Graphics / Vision",
    "CS",
    "https://cpsc.yale.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["brown university"],
    "Brown Computer Graphics Group",
    "CS",
    "https://cs.brown.edu/research/graphics/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["university of wisconsin", "uw–madison", "uw-madison"],
    "Wisconsin Graphics Group",
    "CS",
    "https://graphics.cs.wisc.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Rendering / Imaging", "graphics": True},
    ],
)
F(
    ["uc santa barbara", "ucsb"],
    "UCSB Four Eyes / Graphics",
    "CS",
    "https://www.cs.ucsb.edu/research",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision / HCI",
    ],
)
F(
    ["uc irvine"],
    "UCI Graphics & Visualization",
    "CS",
    "https://www.cs.uci.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["duke university"],
    "Duke Graphics / Visualization",
    "CS",
    "https://cs.duke.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["rice university"],
    "Rice Graphics / Vision",
    "CS",
    "https://www.cs.rice.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["university of maryland"],
    "UMD Graphics & Visual Analytics",
    "CS",
    "https://www.cs.umd.edu/research",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["purdue university"],
    "Purdue Computer Graphics & Visualization",
    "CS",
    "https://www.cs.purdue.edu/research/areas.html",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["texas a&m"],
    "Texas A&M Graphics",
    "CSE",
    "https://engineering.tamu.edu/cse/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Visualization",
    ],
)
F(
    ["ohio state"],
    "OSU Graphics & Visualization",
    "CSE",
    "https://cse.osu.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["northwestern university"],
    "Northwestern Graphics / Vision",
    "CS",
    "https://www.mccormick.northwestern.edu/computer-science/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["boston university"],
    "BU Image & Video / Graphics",
    "CS",
    "https://www.bu.edu/cs/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["northeastern university"],
    "Northeastern Khoury Graphics / Vision",
    "Khoury",
    "https://www.khoury.northeastern.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["stony brook"],
    "Stony Brook Computer Graphics",
    "CS",
    "https://www.cs.stonybrook.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["rpi", "rensselaer"],
    "RPI Computer Graphics",
    "CS",
    "https://www.cs.rpi.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["unc chapel hill", "university of north carolina"],
    "UNC Graphics & Imaging",
    "CS",
    "https://cs.unc.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Medical Graphics / Imaging", "graphics": True},
    ],
)
F(
    ["cu boulder", "university of colorado"],
    "CU Boulder Graphics Lab",
    "CS",
    "https://www.colorado.edu/cs/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["university of virginia"],
    "UVA Graphics / Vision",
    "CS",
    "https://engineering.virginia.edu/cs",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["penn state"],
    "Penn State Graphics / Visualization",
    "CSE",
    "https://www.eecs.psu.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["arizona state"],
    "ASU Graphics / Vision",
    "CSE",
    "https://scai.engineering.asu.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["university of florida"],
    "UF CISE Graphics",
    "CISE",
    "https://www.cise.ufl.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["university of minnesota"],
    "UMN Graphics & Vision",
    "CS",
    "https://cse.umn.edu/cs",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["uc davis"],
    "UC Davis VIDI / Graphics",
    "CS",
    "https://cs.ucdavis.edu/",
    [
        {"text": "Visualization / Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["uc santa cruz"],
    "UCSC Computational Media / Graphics",
    "CSE / CM",
    "https://www.soe.ucsc.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Games / HCI",
    ],
)
F(
    ["vanderbilt"],
    "Vanderbilt Graphics / Vision",
    "CS",
    "https://engineering.vanderbilt.edu/cs/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["rutgers"],
    "Rutgers Graphics Lab",
    "CS",
    "https://www.cs.rutgers.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Animation / Simulation", "graphics": True},
    ],
)
F(
    ["nc state"],
    "NC State Graphics",
    "CS",
    "https://www.csc.ncsu.edu/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision",
    ],
)
F(
    ["georgia tech ece"],
    "Georgia Tech ECE computational imaging / vision faculty",
    "ECE",
    "https://ece.gatech.edu/",
    [
        {"text": "Computational Imaging", "graphics": True},
        "Machine Learning",
    ],
)

# ========== EUROPE ==========
F(
    ["eth zurich"],
    "Olga Sorkine-Hornung",
    "Professor, Interactive Geometry Lab",
    "https://igl.ethz.ch/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Geometry Processing", "graphics": True},
        {"text": "Shape Modeling / Fabrication", "graphics": True},
    ],
    recruiting=True,
)
F(
    ["eth zurich"],
    "Markus Gross / Disney Research & ETH CGL",
    "Professor, Computer Graphics Laboratory",
    "https://cgl.ethz.ch/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Animation / Rendering", "graphics": True},
    ],
)
F(
    ["eth zurich"],
    "Siyu Tang",
    "Assistant Professor (typical; verify)",
    "https://ait.ethz.ch/",
    [
        {"text": "3D Human / Digital Humans", "graphics": True},
        "Computer Vision",
        "AI",
    ],
)
F(
    ["epfl"],
    "Wenzel Jakob",
    "Associate Professor, Realistic Graphics Lab",
    "https://rgl.epfl.ch/",
    [
        {"text": "Physically Based Rendering", "graphics": True},
        {"text": "Differentiable / Inverse Rendering", "graphics": True},
        {"text": "Appearance Modeling", "graphics": True},
    ],
    notes="Mitsuba renderer",
    recruiting=True,
)
F(
    ["epfl"],
    "EPFL Visual Computing / IVRL faculty",
    "IC School",
    "https://www.epfl.ch/schools/ic/",
    [
        {"text": "Visual Computing", "graphics": True},
        "Computer Vision",
        "Graphics",
    ],
)
F(
    ["university of cambridge"],
    "Rafał Mantiuk / Cambridge Graphics & Displays",
    "Professor (verify current)",
    "https://www.cl.cam.ac.uk/",
    [
        {"text": "Neural Rendering / Perception", "graphics": True},
        {"text": "Computer Graphics", "graphics": True},
    ],
)
F(
    ["university of oxford"],
    "Oxford Visual Geometry / Graphics-related faculty",
    "CS",
    "https://www.robots.ox.ac.uk/~vgg/",
    [
        {"text": "3D Vision", "graphics": True},
        "Computer Vision",
    ],
)
F(
    ["imperial college"],
    "Imperial Visual Computing / Graphics",
    "Computing",
    "https://www.imperial.ac.uk/computing/",
    [
        {"text": "Computer Graphics", "graphics": True},
        "Vision / AI",
    ],
)
F(
    ["technical university of munich", "(tum)"],
    "TUM Visual Computing / Graphics faculty",
    "Informatics",
    "https://www.cs.tum.de/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "3D Vision", "graphics": True},
    ],
)
F(
    ["max planck institute for informatics", "mpi-inf"],
    "Christian Theobalt",
    "Director, Visual Computing & AI",
    "https://www.mpi-inf.mpg.de/departments/visual-computing-and-artificial-intelligence",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Digital Humans / Neural Rendering", "graphics": True},
        "Computer Vision",
        "AI",
    ],
    recruiting=True,
)
F(
    ["max planck institute for informatics", "mpi-inf"],
    "Hans-Peter Seidel / Karol Myszkowski (Graphics)",
    "MPI-INF Graphics",
    "https://www.mpi-inf.mpg.de/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Rendering / Perception", "graphics": True},
    ],
)
F(
    ["tu wien"],
    "TU Wien Computer Graphics",
    "Institute for Visual Computing",
    "https://www.cg.tuwien.ac.at/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization / Real-time Graphics", "graphics": True},
    ],
    recruiting=True,
)
F(
    ["inria"],
    "Inria Graphics / Geometry / Vision teams",
    "Multiple centers",
    "https://jobs.inria.fr/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Geometry Processing", "graphics": True},
        "Vision",
    ],
)
F(
    ["kth royal"],
    "KTH Computer Vision / Graphics faculty",
    "EECS",
    "https://www.kth.se/",
    [
        "Computer Vision",
        {"text": "Graphics-related Visual Computing", "graphics": True},
        "AI",
    ],
)
F(
    ["ku leuven"],
    "KU Leuven EAVISE / Graphics & Vision",
    "ESAT",
    "https://www.kuleuven.be/",
    [
        {"text": "Computer Graphics / 3DGS avatars", "graphics": True},
        "Computer Vision",
        "AI",
    ],
)
F(
    ["university of copenhagen"],
    "UCPH IMAGE / Visual Computing",
    "DIKU",
    "https://di.ku.dk/",
    [
        {"text": "Differentiable Rendering", "graphics": True},
        "Machine Learning",
        "Vision",
    ],
)
F(
    ["delft university", "tu delft"],
    "TU Delft Computer Graphics & Visualization",
    "EEMCS",
    "https://www.tudelft.nl/",
    [
        {"text": "Computer Graphics", "graphics": True},
        {"text": "Visualization", "graphics": True},
    ],
)
F(
    ["university of amsterdam", "(uva)"],
    "UvA VIS / AI vision faculty",
    "Informatics",
    "https://www.uva.nl/",
    [
        "Computer Vision",
        "Generative AI",
        {"text": "3D / Visual Computing", "graphics": True},
    ],
)
F(
    ["ellis"],
    "ELLIS units (graphics/vision PIs across Europe)",
    "Network",
    "https://ellis.eu/",
    [
        "Machine Learning",
        {"text": "Visual Computing (selected units)", "graphics": True},
    ],
)

meta = {
    "count": len(faculty),
    "graphicsCount": sum(1 for f in faculty if f["hasGraphics"]),
    "note": "图形学相关研究方向在界面中加粗显示；名单为申请导向抽样，非全系花名册。请以官网为准。",
    "generated": "2026-09-13",
}

(out / "faculty.js").write_text(
    "window.FACULTY_DATA = "
    + json.dumps(faculty, ensure_ascii=False, indent=2)
    + ";\nwindow.FACULTY_META = "
    + json.dumps(meta, ensure_ascii=False, indent=2)
    + ";\n",
    encoding="utf-8",
)
print("faculty", len(faculty), "graphics", meta["graphicsCount"])
