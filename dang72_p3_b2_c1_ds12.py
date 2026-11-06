import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang72_p3_b2_c1_ds12(self):
    # Công thức nghiệm: x = (v1 * AH) / sqrt(v2^2 - v1^2)
    list_data = [
        (12, 20, 30, 50),   # Nghiệm x = 9 (Bài gốc)
        (16, 25, 30, 50),   # Nghiệm x = 12
        (20, 35, 30, 50),   # Nghiệm x = 15
        (24, 30, 50, 130)   # Nghiệm x = 10
    ]

    # Random chọn 1 bộ số
    h, d, v1, v2 = random.choice(list_data)

    # Tính toán các thông số của bài toán dựa trên công thức toán học
    mau_so = math.sqrt(v2**2 - v1**2)
    x_correct = int((v1 * h) / mau_so)

    # Các hằng số phục vụ việc xuất chi tiết các bước trong lời giải
    v2_binh = v2**2
    v1_binh = v1**2
    h_binh = h**2
    hso_x2_cuoicung = v2_binh - v1_binh
    hangso_ve2 = v1_binh * h_binh

    # Các đáp án trắc nghiệm
    da = '$%s$' % (x_correct)

    # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
    # Tạo các phương án nhiễu
    s_raw = [
        '$%s$' % (x_correct + 1),
        '$%s$' % (x_correct - 1),
        '$%s$' % (x_correct + 2),
        '$%s$' % (x_correct - 2),
        '$%s$' % (x_correct + 3),
        '$%s$' % (h),          # Học sinh dễ nhầm lấy luôn cạnh AH
        '$%s$' % (int(d/2))    # Học sinh dễ nhầm lấy trung điểm HB
    ]

    # Lọc bỏ các đáp án trùng lặp và loại trừ trường hợp phương án sai vô tình bằng phương án đúng
    s_unique = list(set(s_raw) - {da})

    das1 = random.choice(s_unique)
    s_unique.remove(das1)
    das2 = random.choice(s_unique)
    s_unique.remove(das2)
    das3 = random.choice(s_unique)

    # Nội dung câu hỏi
    noidungcauhoi = ('''\\immini{Trong một cuộc diễn tập quân sự, một chiếc xe tăng cần di chuyển từ vị trí $A$ (nằm trong khu vực sình lầy) đến vị trí $B$ (nằm trên một con đường nhựa thẳng) để tập kết. Biết rằng hình chiếu vuông góc của $A$ lên con đường nhựa là điểm $H$. Khoảng cách từ $A$ đến $H$ là $AH = %s$ km, và khoảng cách từ $H$ đến $B$ là $HB = %s$ km. Do điều kiện địa hình, vận tốc tối đa của xe tăng khi di chuyển trên khu vực sình lầy là $v_1 = %s$ km/h, trong khi vận tốc tối đa trên đường nhựa là $v_2 = %s$ km/h. Để tiết kiệm thời gian nhất, người lái xe tăng quyết định đi thẳng từ $A$ đến một điểm $M$ nằm trên đoạn đường nhựa $HB$, sau đó tiếp tục đi từ $M$ đến $B$. Hỏi điểm $M$ phải cách $H$ một khoảng bằng bao nhiêu km để tổng thời gian xe tăng di chuyển từ $A$ đến $B$ là ít nhất?}
                     {	\\begin{tikzpicture}[x=1pt,y=-1pt,line cap=round,line join=round, scale=0.35]
                     		\\definecolor{sky}{HTML}{95D2FB}
                     		\\definecolor{halo}{HTML}{B6E7F2}
                     		\\definecolor{shadow}{HTML}{46A6CE}
                     		\\definecolor{track}{HTML}{243F4B}
                     		\\definecolor{tread}{HTML}{354D59}
                     		\\definecolor{treadlight}{HTML}{45606A}
                     		\\definecolor{deepgreen}{HTML}{294B32}
                     		\\definecolor{darkgreen}{HTML}{44653A}
                     		\\definecolor{green}{HTML}{64834A}
                     		\\definecolor{olive}{HTML}{86A25D}
                     		\\definecolor{lightolive}{HTML}{ADC778}
                     		\\definecolor{cream}{HTML}{E8EE9B}
                     		\\definecolor{rim}{HTML}{967662}
                     		\\definecolor{rubber}{HTML}{304B57}
                     		\\definecolor{wheel}{HTML}{DFB89C}
                     		\\definecolor{hub}{HTML}{A07D66}
                     		\\definecolor{glass}{HTML}{C7AED8}
                     		\\definecolor{red}{HTML}{D52F55}
                     	\\path[use as bounding box] (0,0) rectangle (547,382);
                     	\\clip (0,0) rectangle (547,382);
                     	\\fill[sky] (0,0) rectangle (547,382);
                     	\\begin{scope}
                     		\\clip (0,0) rectangle (547,344);
                     		\\fill[halo] (262,226) circle[radius=187pt];
                     	\\end{scope}
                     	\\fill[shadow] (24,346) .. controls (166,341) and (340,344) .. (512,345)
                     	.. controls (517,345) and (518,351) .. (512,351)
                     	-- (219,366) -- (23,353) .. controls (18,352) and (19,347) .. cycle;
                     	\\fill[track] (53,262) .. controls (70,249) and (114,242) .. (161,248)
                     	-- (260,277) -- (262,335) -- (232,345) -- (109,345)
                     	.. controls (67,337) and (40,315) .. (31,293) -- cycle;
                     	\\fill[tread] (63,280) -- (84,318) -- (118,338) -- (223,342)
                     	-- (246,329) -- (235,281) -- cycle;
                     	\\foreach \\wheelx/\\wheely in {130/308,181/306,224/306}{
                     		\\fill[rubber] (\\wheelx,\\wheely) ellipse[x radius=24pt,y radius=32pt];
                     		\\fill[rim] (\\wheelx,\\wheely) ellipse[x radius=18pt,y radius=27pt];
                     		\\fill[wheel] (\\wheelx,\\wheely) ellipse[x radius=13pt,y radius=22pt];
                     		\\fill[hub] (\\wheelx,\\wheely) ellipse[x radius=7pt,y radius=11pt];
                     		\\fill[wheel] (\\wheelx,\\wheely) ellipse[x radius=4pt,y radius=7pt];}
                     	\\fill[tread] (29,265) -- (64,258) -- (71,285) -- (86,309)
                     	-- (111,338) -- (92,335) -- (62,324) -- (42,308) -- (30,288) -- cycle;
                     	\\draw[track,line width=2pt] (30,287) -- (70,286);
                     	\\draw[track,line width=2pt] (34,301) -- (78,300);
                     	\\draw[track,line width=2pt] (43,315) -- (88,314);
                     	\\draw[track,line width=2pt] (59,328) -- (99,327);
                     	\\draw[track,line width=1.3pt] (81,338) -- (107,338);
                     	\\fill[darkgreen] (404,241) .. controls (406,230) and (411,222) .. (424,222)
                     	-- (450,224) .. controls (466,224) and (473,232) .. (476,245) -- cycle;
                     	\\fill[lightolive] (404,239) .. controls (407,228) and (412,223) .. (422,222)
                     	.. controls (416,226) and (411,231) .. (410,241) -- cycle;
                     	\\fill[deepgreen] (203,204) -- (215,188) -- (235,181) -- (261,187)
                     	-- (267,219) -- (252,232) -- (206,226) -- (201,217) -- cycle;
                     	\\fill[green] (204,204) -- (216,193) -- (234,184) -- (241,209)
                     	-- (226,218) -- (204,218) -- (198,211) -- cycle;
                     	\\fill[cream] (197,205) -- (211,200) -- (208,211) -- (204,215) -- cycle;
                     	\\fill[deepgreen] (211,215) -- (217,193) -- (224,192) -- (218,211) -- cycle;
                     	\\fill[darkgreen] (230,198) .. controls (224,208) and (238,214) .. (242,226)
                     	-- (276,232) -- (301,215) -- (280,180) -- (242,178) -- cycle;
                     	\\draw[deepgreen,line width=2pt] (228,198) .. controls (232,207) and (239,210) .. (248,210);
                     	\\fill[deepgreen] (240,170) -- (240,162) -- (267,159) -- (283,162) -- (282,175) -- cycle;
                     	\\fill[glass] (245,163) -- (262,161) -- (261,167) -- (245,169) -- cycle;
                     	\\fill[green] (247,172) .. controls (260,161) and (281,158) .. (295,164)
                     	-- (296,183) -- (254,186) -- cycle;
                     	\\fill[cream] (249,172) .. controls (260,166) and (274,164) .. (285,166)
                     	-- (282,170) -- (267,170) -- (264,179) -- cycle;
                     	\\draw[darkgreen,line width=1pt] (263,169) -- (288,167);
                     	\\fill[deepgreen] (283,170) -- (324,166) -- (356,166)
                     	-- (378,184) -- (389,208) -- (376,231) -- (293,230)
                     	.. controls (279,220) and (269,212) .. (271,200)
                     	-- (276,179) .. controls (278,172) and (279,171) .. cycle;
                     	\\fill[olive] (286,174) -- (324,168) -- (353,168)
                     	-- (376,181) -- (389,190) -- (397,207) -- (383,226)
                     	-- (298,225) .. controls (282,217) and (274,207) .. (277,197) -- (282,180) -- cycle;
                     	\\fill[green] (285,211) .. controls (294,214) and (303,221) .. (319,219)
                     	-- (333,208) -- (351,209) -- (363,217) -- (384,217)
                     	-- (396,206) -- (384,226) -- (298,225) -- cycle;
                     	\\fill[lightolive] (364,181) -- (384,185) -- (381,193) -- (377,193)
                     	-- (382,205) -- (362,206) -- (354,190) -- cycle;
                     	\\fill[cream] (371,183) -- (382,179) -- (387,183) -- (389,189)
                     	-- (372,189) .. controls (368,189) and (367,186) .. cycle;
                     	\\fill[deepgreen] (300,179) -- (326,177) -- (333,209) -- (306,213) -- cycle;
                     	\\fill[cream] (303,181) -- (325,180) -- (327,199) -- (301,200) -- cycle;
                     	\\fill[darkgreen] (301,200) -- (327,199) -- (329,208) -- (307,212) -- cycle;
                     	\\fill[deepgreen] (330,178) -- (356,179) -- (365,200) -- (361,212) -- (338,209) -- cycle;
                     	\\fill[cream] (332,180) -- (355,180) -- (363,200) -- (340,198) -- cycle;
                     	\\fill[green] (340,198) -- (364,200) -- (361,209) -- (338,207) -- cycle;
                     	\\draw[deepgreen,line width=1pt] (331,181) -- (335,207);
                     	\\fill[deepgreen] (346,168) -- (348,151) -- (357,151) -- (357,159)
                     	-- (361,161) -- (361,169) -- cycle;
                     	\\fill[darkgreen] (350,153) -- (353,57) -- (354,57) -- (353,154) -- cycle;
                     	\\fill[deepgreen] (310,146) -- (312,141) -- (323,140) -- (327,144)
                     	-- (337,140) -- (345,143) -- (347,159) -- cycle;
                     	\\fill[olive] (302,145) -- (331,142) -- (347,149) -- (352,162)
                     	-- (348,171) -- (327,169) -- (298,176) -- cycle;
                     	\\fill[darkgreen] (302,145) -- (330,143) -- (331,170) -- (301,174) -- cycle;
                     	\\fill[deepgreen] (306,148) -- (328,146) -- (327,170) -- (304,172) -- cycle;
                     	\\fill[glass] (311,151) -- (325,149) -- (325,168) -- (311,169) -- cycle;
                     	\\fill[deepgreen] (338,159) ellipse[x radius=2.2pt,y radius=2.7pt];
                     	\\fill[darkgreen] (46,108) -- (260,182)
                     	.. controls (267,185) and (268,193) .. (261,197)
                     	.. controls (256,201) and (248,197) .. (241,194) -- (39,132) -- cycle;
                     	\\fill[olive] (43,104) -- (260,179)
                     	.. controls (264,181) and (267,186) .. (266,190) -- (252,190) -- (45,119) -- cycle;
                     	\\fill[cream] (43,104) -- (262,179) -- (265,183) -- (43,108) -- cycle;
                     	\\fill[green] (146,139) -- (192,155)
                     	.. controls (198,163) and (194,176) .. (187,181)
                     	-- (139,166) .. controls (147,157) and (149,148) .. cycle;
                     	\\fill[darkgreen] (143,152) -- (194,169)
                     	.. controls (194,175) and (191,179) .. (186,182) -- (138,167) -- cycle;
                     	\\draw[deepgreen,line width=1.8pt] (192,157) .. controls (199,164) and (196,176) .. (188,180);
                     	\\draw[deepgreen,line width=1.6pt] (140,139) .. controls (150,148) and (146,161) .. (137,164);
                     	\\draw[deepgreen,line width=1.4pt] (242,175) .. controls (253,177) and (254,193) .. (242,195);
                     	\\fill[darkgreen] (37,103) -- (60,111)
                     	.. controls (65,118) and (61,131) .. (55,135) -- (31,128) -- cycle;
                     	\\fill[lightolive] (36,103) -- (59,110) -- (60,118) -- (39,113) -- cycle;
                     	\\fill[olive] (32,102) .. controls (41,101) and (47,109) .. (45,118)
                     	.. controls (43,128) and (37,133) .. (29,129)
                     	.. controls (22,127) and (20,121) .. (23,112)
                     	.. controls (25,106) and (27,103) .. cycle;
                     	\\fill[lightolive] (33,106) .. controls (39,105) and (41,111) .. (39,117)
                     	.. controls (37,124) and (31,126) .. (27,121)
                     	.. controls (25,118) and (29,108) .. cycle;
                     	\\fill[deepgreen] (33,109) .. controls (38,109) and (38,114) .. (35,119)
                     	.. controls (33,123) and (28,122) .. (29,117)
                     	.. controls (29,113) and (30,110) .. cycle;
                     	\\draw[deepgreen,line width=1.6pt] (59,113) .. controls (63,118) and (60,129) .. (55,132);
                     	\\fill[green] (76,265) -- (130,242) -- (164,230) -- (222,218)
                     	-- (269,220) -- (309,224) -- (349,221) -- (408,227)
                     	-- (414,247) -- (222,270) -- (104,286) -- cycle;
                     	\\fill[olive] (28,252) -- (63,242) -- (103,237) -- (130,235)
                     	-- (148,228) -- (204,226) -- (225,225) -- (245,221)
                     	-- (349,230) -- (416,236) -- (412,246) -- (290,244)
                     	-- (219,248) -- (160,263) -- (78,278) -- (37,270) -- (18,262) -- cycle;
                     	\\fill[lightolive] (25,256) -- (54,243) -- (95,238) -- (119,239)
                     	-- (139,233) -- (151,233) -- (150,243) -- (119,249)
                     	-- (89,252) -- (60,261) -- cycle;
                     	\\fill[cream] (25,256) -- (54,245) -- (77,242) -- (71,245)
                     	-- (49,252) -- (35,260) -- cycle;
                     	\\fill[cream] (52,249) -- (68,246) -- (65,250) -- (52,254) -- (50,253) -- cycle;
                     	\\fill[green] (58,259) -- (73,248) -- (88,246) -- (82,255)
                     	-- (101,255) -- (121,250) -- (133,250) -- (136,258) -- (96,273) -- (73,274) -- cycle;
                     	\\fill[deepgreen] (28,263) -- (55,262) -- (65,271) -- (28,275) -- cycle;
                     	\\fill[deepgreen] (151,233) -- (154,220) -- (190,219) -- (189,231) -- cycle;
                     	\\fill[cream] (157,223) -- (181,222) -- (184,227) -- (156,228) -- cycle;
                     	\\fill[lightolive] (188,229) -- (218,226) -- (239,225) -- (254,222)
                     	-- (323,229) -- (346,231) -- (343,236) -- (245,230) -- (207,234) -- (184,235) -- cycle;
                     	\\fill[cream] (196,228) -- (215,225) -- (215,229) -- (202,231) -- (187,233) -- cycle;
                     	\\fill[cream] (232,227) .. controls (234,222) and (241,222) .. (244,226)
                     	-- (251,228) -- (251,230) -- (239,228) -- cycle;
                     	\\fill[cream] (295,231) .. controls (297,226) and (301,226) .. (307,228) -- (314,232) -- cycle;
                     	\\fill[green] (300,230) circle[radius=1.4pt];
                     	\\fill[green] (307,231) circle[radius=1.4pt];
                     	\\fill[darkgreen] (69,269) -- (115,250) -- (155,251) -- (201,257)
                     	-- (227,292) -- (234,325) -- (211,327) -- (180,315)
                     	-- (109,315) -- (83,306) -- (74,290) -- cycle;
                     	\\fill[olive] (77,272) -- (111,254) -- (150,254) -- (182,258)
                     	-- (185,285) -- (169,316) -- (111,315) -- (89,305) -- cycle;
                     	\\fill[lightolive] (76,272) -- (112,253) -- (116,258) -- (102,272) -- cycle;
                     	\\fill[lightolive] (112,272) .. controls (128,259) and (143,255) .. (162,255)
                     	-- (169,260) -- (146,263) -- (144,273) -- cycle;
                     	\\fill[cream] (117,269) .. controls (128,262) and (138,256) .. (149,257)
                     	-- (151,260) .. controls (142,260) and (135,264) .. (140,270)
                     	-- (128,274) -- (115,274) -- cycle;
                     	\\fill[green] (118,274) -- (145,274) -- (153,285)
                     	.. controls (152,290) and (141,291) .. (137,289) -- (124,289) -- cycle;
                     	\\fill[darkgreen] (93,276) .. controls (84,281) and (96,289) .. (105,292)
                     	.. controls (114,296) and (112,299) .. (104,300)
                     	-- (112,311) -- (124,316) -- (99,313) -- (84,300) -- (76,279) -- cycle;
                     	\\fill[darkgreen] (141,298) .. controls (149,293) and (160,299) .. (168,297)
                     	-- (172,316) -- (139,315) .. controls (133,310) and (135,302) .. cycle;
                     	\\fill[rim] (75,282) .. controls (77,296) and (86,309) .. (97,310)
                     	-- (93,303) -- (82,289) -- cycle;
                     	\\fill[track] (171,254) -- (226,245) -- (273,256) -- (458,256)
                     	-- (485,267) -- (480,301) .. controls (476,322) and (453,342) .. (435,348)
                     	-- (247,348) .. controls (215,344) and (186,328) .. (172,307)
                     	.. controls (159,286) and (156,267) .. cycle;
                     	\\fill[tread] (169,257) -- (216,253) -- (215,280)
                     	.. controls (216,305) and (233,326) .. (248,339)
                     	-- (228,344) .. controls (200,334) and (177,316) .. (168,295)
                     	.. controls (161,280) and (159,267) .. cycle;
                     	\\draw[track,line width=2pt] (162,269) -- (210,269);
                     	\\draw[track,line width=2pt] (163,284) -- (211,284);
                     	\\draw[track,line width=2pt] (167,299) -- (214,299);
                     	\\draw[track,line width=2pt] (175,314) -- (222,314);
                     	\\draw[track,line width=2pt] (188,328) -- (233,328);
                     	\\draw[track,line width=2pt] (209,339) -- (242,339);
                     	\\fill[treadlight] (240,335) -- (441,336) -- (427,344) -- (249,344) -- cycle;
                     	\\foreach \\treadx in {258,276,294,312,330,348,366,384,402,420}{
                     		\\draw[track,line width=1.1pt] (\\treadx,337) -- (\\treadx,343); }
                     	\\foreach \\offset in {0,1,2,3,4,5}{
                     		\\draw[treadlight,line width=1.1pt]
                     		({449+4.4*\\offset},{329-4.4*\\offset}) -- ++(5,3); }
                     	\\fill[rubber] (233,279) ellipse[x radius=25pt,y radius=35pt];
                     	\\fill[rim] (232,280) ellipse[x radius=18pt,y radius=26pt];
                     	\\fill[wheel] (229,279) ellipse[x radius=12pt,y radius=22pt];
                     	\\fill[hub] (227,282) ellipse[x radius=7pt,y radius=10pt];
                     	\\fill[wheel] (226,282) ellipse[x radius=4pt,y radius=6pt];
                     	\\foreach \\wheelx/\\wheely/\\radiusx/\\radiusy in {278/314/24/31,328/315/24/31,377/315/23/30,426/315/22/29}{
                     		\\fill[rubber] (\\wheelx,\\wheely) ellipse[x radius=\\radiusx pt,y radius=\\radiusy pt];
                     		\\fill[rim] (\\wheelx,\\wheely) ellipse[x radius=16.5pt,y radius=23pt];
                     		\\fill[wheel] ({\\wheelx-2},\\wheely) ellipse[x radius=12pt,y radius=19pt];
                     		\\fill[hub] ({\\wheelx-3},\\wheely) ellipse[x radius=6.8pt,y radius=9pt];
                     		\\fill[wheel] ({\\wheelx-4},\\wheely) ellipse[x radius=3.8pt,y radius=5.5pt];}
                     	\\fill[green] (461,291) ellipse[x radius=18pt,y radius=22pt];
                     	\\draw[cream,line width=5pt,dash pattern=on 2pt off 3pt] (461,291)
                     	ellipse[x radius=13.5pt,y radius=17pt];
                     	\\fill[olive] (460,291) ellipse[x radius=11pt,y radius=14pt];
                     	\\fill[darkgreen] (460,290) ellipse[x radius=5pt,y radius=8pt];
                     	\\fill[rim] (460,288) ellipse[x radius=3.7pt,y radius=5pt];
                     	\\fill[cream] (462,296) circle[radius=1.5pt];
                     	\\fill[cream] (454,292) circle[radius=1.4pt];
                     	\\fill[cream] (464,283) circle[radius=1.4pt];
                     	\\fill[deepgreen] (153,260) -- (164,250) -- (215,236) -- (232,243)
                     	-- (208,269) -- (163,269) -- cycle;
                     	\\fill[green] (145,253) -- (180,236) -- (218,230) -- (244,231)
                     	-- (259,237) -- (226,247) -- (206,263) -- (157,263) -- cycle;
                     	\\fill[lightolive] (146,253) -- (179,237) -- (218,232) -- (240,231)
                     	-- (244,234) -- (218,239) -- (204,238) -- (181,244) -- (166,255) -- cycle;
                     	\\fill[cream] (144,254) -- (158,247) -- (163,247) -- (159,255) -- (151,259) -- cycle;
                     	\\fill[darkgreen] (161,260) -- (175,252) -- (205,241) -- (216,242) -- (225,254) -- (208,262) -- cycle;
                     	\\fill[darkgreen] (222,242) -- (254,230) -- (408,239) -- (494,246)
                     	-- (503,250) -- (507,276) -- (476,284) -- (432,278)
                     	-- (379,282) -- (306,279) -- (263,273) -- (236,278) -- (229,268) -- cycle;
                     	\\fill[olive] (228,242) -- (254,232) -- (400,240) -- (493,246)
                     	-- (501,249) -- (498,267) -- (476,280) -- (436,274)
                     	-- (382,278) -- (310,276) -- (265,270) -- (237,274) -- cycle;
                     	\\fill[green] (231,247) -- (254,239) -- (280,243)
                     	.. controls (283,254) and (269,262) .. (277,272)
                     	-- (260,268) -- (243,272) -- (237,268) -- cycle;
                     	\\fill[lightolive] (254,234) -- (401,242) -- (496,249) -- (501,253)
                     	-- (398,247) -- (256,238) -- (229,246) -- (228,242) -- cycle;
                     	\\draw[green,line width=1pt] (260,235) -- (398,243) -- (498,250);
                     	\\fill[green] (287,245) -- (329,246)
                     	.. controls (327,252) and (314,254) .. (311,260)
                     	.. controls (307,264) and (321,268) .. (325,268)
                     	-- (320,274) -- (294,271) -- (286,266) -- cycle;
                     	\\fill[lightolive] (344,245) -- (361,246) -- (367,256)
                     	.. controls (375,263) and (392,254) .. (397,261)
                     	.. controls (392,269) and (376,271) .. (365,273) -- (349,269) -- cycle;
                     	\\fill[cream] (339,245) -- (345,244) -- (345,253) -- (342,264)
                     	-- (337,267) -- (332,267) -- (331,264) -- (337,262) -- cycle;
                     	\\fill[cream] (349,245) -- (361,247) -- (364,251) -- (362,256)
                     	-- (370,263) -- (370,267) -- (350,264) -- cycle;
                     	\\draw[darkgreen,line width=1.5pt] (344,246) -- (348,275);
                     	\\fill[green] (395,247) -- (430,248) -- (426,267)
                     	.. controls (415,277) and (397,277) .. (381,277)
                     	-- (368,273) .. controls (382,273) and (395,269) .. (398,262) -- cycle;
                     	\\fill[lightolive] (439,250) -- (460,253) -- (451,266) -- (453,274)
                     	-- (437,271) -- (433,267) -- cycle;
                     	\\fill[cream] (439,251) -- (445,251) -- (440,265) -- (434,267) -- cycle;
                     	\\fill[green] (470,253) -- (498,256) -- (499,266) -- (479,273)
                     	-- (462,272) -- (465,263) -- cycle;
                     	\\draw[darkgreen,line width=1pt] (436,248) -- (430,271);
                     	\\fill[cream] (278,232) -- (282,241) -- (292,242) -- (284,249)
                     	-- (286,261) -- (278,254) -- (269,260) -- (272,249)
                     	-- (265,242) -- (275,241) -- cycle;
                     	\\fill[red] (278,235) -- (281,243) -- (289,243) -- (282,248)
                     	-- (284,257) -- (278,252) -- (271,257) -- (274,248)
                     	-- (268,243) -- (276,243) -- cycle;
                     	\\fill[deepgreen] (59,271) -- (99,245) -- (105,253) -- (65,279) -- cycle;
                     	\\fill[cream] (57,268) -- (97,242) -- (103,245) -- (63,274) -- cycle;
                     	\\fill[darkgreen] (108,232) .. controls (116,232) and (122,239) .. (122,246)
                     	-- (112,255) -- (103,252) -- cycle;
                     	\\fill[deepgreen] (106,244) ellipse[x radius=10pt,y radius=12pt];
                     	\\fill[lightolive] (105,244) ellipse[x radius=9pt,y radius=11pt];
                     	\\fill[darkgreen] (107,245) ellipse[x radius=6.5pt,y radius=9.5pt];
                     	\\fill[glass] (105,245) ellipse[x radius=5.5pt,y radius=8pt];
                     \\end{tikzpicture}}'''
        % (h, d, v1, v2))

    # Gắn tag \True vào đáp án đúng
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2) 
    da_s3 = str(das3) 

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải (Áp dụng toán học Đạo hàm)
    loigiai = ('''Gọi độ dài đoạn $HM = x$ (km), với điều kiện $0 \\le x \\le %s$.\\\\
    Khi đó, khoảng cách từ $M$ đến $B$ là $MB = %s - x$ (km).\\\\
    Quãng đường xe tăng di chuyển qua khu vực sình lầy là đoạn $AM$. Áp dụng định lý Pytago trong tam giác vuông $AHM$, ta có:
    $$AM = \\sqrt{AH^2 + HM^2} = \\sqrt{%s + x^2} \\text{ (km)}$$
    Thời gian xe tăng đi trên sình lầy (từ $A$ đến $M$) là:
    $$t_1 = \\frac{AM}{v_1} = \\frac{\\sqrt{%s + x^2}}{%s} \\text{ (giờ)}$$
    Thời gian xe tăng đi trên đường nhựa (từ $M$ đến $B$) là:
    $$t_2 = \\frac{MB}{v_2} = \\frac{%s - x}{%s} \\text{ (giờ)}$$
    Tổng thời gian di chuyển từ $A$ đến $B$ là một hàm số theo biến $x$:
    $$T(x) = \\frac{\\sqrt{%s + x^2}}{%s} + \\frac{%s - x}{%s}$$
    Để tìm thời gian di chuyển ít nhất, ta cần tìm giá trị nhỏ nhất của hàm số $T(x)$ trên đoạn $[0; %s]$.\\\\
    Tính đạo hàm của $T(x)$:
    $$T'(x) = \\frac{1}{%s} \\cdot \\frac{x}{\\sqrt{%s + x^2}} - \\frac{1}{%s}$$
    Cho $T'(x) = 0$, ta được:
    $$\\frac{x}{%s\\sqrt{%s + x^2}} = \\frac{1}{%s}$$
    $$\\Leftrightarrow %s x = %s\\sqrt{%s + x^2}$$
    Vì $x \\ge 0$, bình phương hai vế ta có:
    $$%s x^2 = %s(%s + x^2)$$
    $$\\Leftrightarrow %s x^2 = %s + %s x^2$$
    $$\\Leftrightarrow %s x^2 = %s$$
    $$\\Leftrightarrow x^2 = %s$$
    $$\\Leftrightarrow x = %s \\text{ (thỏa mãn } 0 \\le x \\le %s \\text{)}$$
    Lập bảng biến thiên hoặc kiểm tra giá trị tại các đầu mút, ta thấy $T(x)$ đạt giá trị nhỏ nhất tại $x = %s$.\\\\
    Vậy điểm $M$ cần cách $H$ một khoảng là $%s$ km thì thời gian xe tăng di chuyển đến điểm tập kết sẽ là ngắn nhất.'''
        % (d, d, h_binh, 
           h_binh, v1, 
           d, v2, 
           h_binh, v1, d, v2, 
           d, 
           v1, h_binh, v2, 
           v1, h_binh, v2, 
           v2, v1, h_binh, 
           v2_binh, v1_binh, h_binh, 
           v2_binh, hangso_ve2, v1_binh, 
           hso_x2_cuoicung, hangso_ve2, 
           x_correct**2, 
           x_correct, d, 
           x_correct, 
           x_correct
          ))
    dapan='\\shortans[0]{$%s$}\n'%(x_correct)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

