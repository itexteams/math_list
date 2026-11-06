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


def bt_dang4_p2_b4_c2_hh12(self):
            # Khai báo biến
            # --- KHAI BÁO BIẾN NGẪU NHIÊN ---
            a = randint(25, 35)
            b = randint(45, 55)
            k = randint(2, 4)
            c = 3 * k
            r = 5 * k
            r_sq = r**2

            # --- NỘI DUNG CÂU HỎI (GIỮ NGUYÊN HÌNH VẼ) ---
            noidungcauhoi = ('''\\immini{Công nghệ hỗ trợ trọng tài VAR (Video Assistant Referee) thiết lập một hệ tọa độ $Oxyz$ để theo dõi vị trí của quả bóng $M$. Cho biết $M$ đang nằm trên mặt sân có phương trình $z=0$, đồng thời thuộc mặt cầu $$(S): (x-%s)^2+(y-%s)^2+(z-%s)^2=%s$$ (đơn vị độ dài tính theo mét).}
                            {\\definecolor{qqffff}{rgb}{0.,1.,1.}
                            \\definecolor{ffffff}{rgb}{1.,1.,1.}
                            \\definecolor{ttzzqq}{rgb}{0.2,0.6,0.}
                            \\definecolor{qqwuqq}{rgb}{0.,0.39215686274509803,0.}
                            \\scalebox{0.4}{
                            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                                    \\clip(0.013432386339273347,-0.1418964287804234) rectangle (13.70769932522624,9.202643730056186);
                                    \\fill[line width=0.pt,color=qqwuqq,fill=qqwuqq,fill opacity=1.0] (0.14,0.) -- (0.18,9.08) -- (13.46,9.12) -- (13.5,0.02) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (0.44,8.84) -- (1.1,8.84) -- (1.0714396362865413,0.2604855223712424) -- (0.4474925833724934,0.24507942229929064) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (1.7372578838749924,8.85819473260321) -- (2.349239154821898,8.847067800404174) -- (2.3603660870209326,0.25707614274942964) -- (1.7150040194769232,0.25707614274942964) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (2.9946012223659073,8.85819473260321) -- (3.6399632899099164,8.847067800404174) -- (3.684471018706055,0.25707614274942964) -- (2.9834742901668725,0.25707614274942964) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (4.263071493055857,8.847067800404174) -- (4.274198425254891,0.2793300071474989) -- (4.930687424997935,0.2793300071474989) -- (4.8849214400107765,8.859452988794228) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (5.54363078066178,8.847783709576083) -- (5.530532445790286,0.28147270361834426) -- (6.237842528851016,0.25527603387535425) -- (6.237842528851016,8.873980379319073) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (6.814169263196797,8.873980379319073) -- (6.839694538548034,0.26321430047553834) -- (7.490929751216832,0.2570120603548831) -- (7.466654562653654,8.884735540530082) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (8.0757277214855,8.842242064332511) -- (8.104056705617214,0.3010533486208074) -- (8.769787832712488,0.28688885655495056) -- (8.75562334064663,8.856406556398369) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (9.407189975676047,8.856406556398369) -- (9.364696499478477,0.27272436448909365) -- (10.044592118639608,0.3152178406866643) -- (10.016263134507895,8.856406556398369) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (10.62533629333974,8.856406556398369) -- (10.62533629333974,0.25855987242323675) -- (11.30523191250087,0.27272436448909365) -- (11.319396404566728,8.828077572266656) -- cycle;
                                    \\fill[line width=0.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.44999998807907104] (11.942634055464431,8.828077572266656) -- (11.914305071332718,0.27272436448909365) -- (12.608365182559705,0.28688885655495056) -- (12.608365182559705,8.856406556398369) -- cycle;
                                    \\draw [line width=2.8pt,color=ffffff,fill=ffffff,fill opacity=1.0] (10.632540693838052,1.3411256894540557) circle (0.276274674326432cm);
                                    \\fill[line width=1.6pt,fill=black,fill opacity=1.0] (10.62135375800568,1.4786728714707718) -- (10.500140755846434,1.3887845777347037) -- (10.547808790403442,1.238970754841257) -- (10.738480928631466,1.2471424179081723) -- (10.771167580899128,1.3996801284905906) -- cycle;
                                    \\draw [line width=2.pt,color=ffffff] (0.44,8.84)-- (13.203273849325695,8.813913080200798);
                                    \\draw [line width=2.pt,color=ffffff] (13.203273849325695,8.813913080200798)-- (13.231602833457409,0.25855987242323675);
                                    \\draw [line width=2.pt,color=ffffff] (13.231602833457409,0.25855987242323675)-- (0.4474925833724934,0.24507942229929064);
                                    \\draw [line width=2.pt,color=ffffff] (0.4474925833724934,0.24507942229929064)-- (0.44,8.84);
                                    \\draw [line width=2.pt,color=ffffff] (6.814169263196797,8.873980379319073)-- (6.839694538548034,0.26321430047553834);
                                    \\draw [line width=2.pt,color=ffffff] (0.44255405640566614,5.91018115564022)-- (1.24844254574248,5.910192206700136);
                                    \\draw [line width=2.pt,color=ffffff] (1.24844254574248,5.910192206700136)-- (1.2463878459891515,3.1886897829983676);
                                    \\draw [line width=2.pt,color=ffffff] (1.2463878459891515,3.1886897829983676)-- (0.44493310800273017,3.18111448925051);
                                    \\draw [line width=2.pt,color=ffffff] (0.44134808251061136,7.293582491530373)-- (2.612665784281165,7.270470251797004);
                                    \\draw [line width=2.pt,color=ffffff] (2.612665784281165,7.270470251797004)-- (2.6357863450598398,1.8486987491977926);
                                    \\draw [line width=2.pt,color=ffffff] (2.6357863450598398,1.8486987491977926)-- (0.4461047166953679,1.837134294337615);
                                    \\draw [line width=2.pt,color=ffffff] (0.4432516705298143,5.109931402938345)-- (0.21685788407982615,5.103434350536642);
                                    \\draw [line width=2.pt,color=ffffff] (0.21685788407982615,5.103434350536642)-- (0.21685788407982615,3.9693515793750893);
                                    \\draw [line width=2.pt,color=ffffff] (0.21685788407982615,3.9693515793750893)-- (0.44425160982297285,3.9628772588668766);
                                    \\draw [line width=2.pt,color=ffffff] (13.208465304142228,7.246093725607949)-- (11.037320602602327,7.256926701149331);
                                    \\draw [line width=2.pt,color=ffffff] (11.037320602602327,7.256926701149331)-- (11.059004679554665,1.8142233861122823);
                                    \\draw [line width=2.pt,color=ffffff] (11.059004679554665,1.8142233861122823)-- (13.226451283677154,1.8143279060603517);
                                    \\draw [line width=2.pt,color=ffffff] (13.212845152457737,5.923379534324272)-- (12.42510152755201,5.890829853151984);
                                    \\draw [line width=2.pt,color=ffffff] (12.42510152755201,5.890829853151984)-- (12.414259489075842,3.191162272585798);
                                    \\draw [line width=2.pt,color=ffffff] (12.414259489075842,3.191162272585798)-- (13.221856270736438,3.2020218141560868);
                                    \\draw [line width=2.pt,color=ffffff] (13.215609720702918,5.088479924279402)-- (13.411727028883428,5.088519005915447);
                                    \\draw [line width=2.pt,color=ffffff] (13.411727028883428,5.088519005915447)-- (13.423091497530072,3.9832429063106214);
                                    \\draw [line width=2.pt,color=ffffff] (13.423091497530072,3.9832429063106214)-- (13.240465313635086,3.97621882231466);
                                    \\draw [line width=2.pt,color=ffffff] (6.826970635842874,4.555530379204722) circle (1.2779536470478101cm);
                                    \\draw [shift={(1.9093380818559327,4.549522677658089)},line width=2.pt,color=ffffff]  plot[domain=-0.9581479715141219:0.9666767044641055,variable=\\t]({1.*1.250869051530642*cos(\\t r)+0.*1.250869051530642*sin(\\t r)},{0.*1.250869051530642*cos(\\t r)+1.*1.250869051530642*sin(\\t r)});
                                    \\draw [shift={(11.757911714402882,4.542435386414702)},line width=2.pt,color=ffffff]  plot[domain=2.1739107206314694:4.117242671879822,variable=\\t]({1.*1.2586272852803428*cos(\\t r)+0.*1.2586272852803428*sin(\\t r)},{0.*1.2586272852803428*cos(\\t r)+1.*1.2586272852803428*sin(\\t r)});
                                    \\draw [line width=2.pt,color=qqffff] (13.5,0.02)-- (10.869227386586182,1.1986226889588785);
                                    \\draw [line width=1.6pt] (10.62135375800568,1.4786728714707718)-- (10.500140755846434,1.3887845777347037);
                                    \\draw [line width=1.6pt] (10.500140755846434,1.3887845777347037)-- (10.547808790403442,1.238970754841257);
                                    \\draw [line width=1.6pt] (10.547808790403442,1.238970754841257)-- (10.738480928631466,1.2471424179081723);
                                    \\draw [line width=1.6pt] (10.738480928631466,1.2471424179081723)-- (10.771167580899128,1.3996801284905906);
                                    \\draw [line width=1.6pt] (10.771167580899128,1.3996801284905906)-- (10.62135375800568,1.4786728714707718);
                                    \\draw [line width=2.pt] (10.62135375800568,1.4786728714707718)-- (10.618629870316708,1.5944380982520714);
                                    \\draw [line width=2.pt] (10.500140755846434,1.3887845777347037)-- (10.384375529065133,1.3983181846461048);
                                    \\draw [line width=2.pt] (10.547808790403442,1.238970754841257)-- (10.474263822801204,1.1640638433945336);
                                    \\draw [line width=2.pt] (10.738480928631466,1.2471424179081723)-- (10.795682570099874,1.1790452256838784);
                                    \\draw [line width=2.pt] (10.771167580899128,1.3996801284905906)-- (10.847436436190339,1.4364526122917094);
                                    \\draw [line width=2.pt] (10.847436436190339,1.4364526122917094)-- (10.83913357125118,1.5245570899184813);
                                    \\draw [line width=2.pt] (10.618629870316708,1.5944380982520714)-- (10.710306391556808,1.6062298047229278);
                                    \\draw [line width=2.pt] (10.618629870316708,1.5944380982520714)-- (10.505529240301904,1.5864739854432697);
                                    \\draw [line width=2.pt] (10.384375529065133,1.3983181846461048)-- (10.395556547014593,1.483133470327263);
                                    \\draw [line width=2.pt] (10.384375529065133,1.3983181846461048)-- (10.356542379897572,1.3287714846561576);
                                    \\draw [line width=2.pt] (10.474263822801204,1.1640638433945336)-- (10.396049076622022,1.1982991839982304);
                                    \\draw [line width=2.pt] (10.474263822801204,1.1640638433945336)-- (10.532827408114096,1.0946047073257539);
                                    \\draw [line width=2.pt] (10.532827408114096,1.0946047073257539)-- (10.701708444830347,1.0959666511702397);
                                    \\begin{scriptsize}
                                        \\draw [fill=ffffff] (2.003985319582601,4.539589173476971) circle (2.5pt);
                                        \\draw [fill=ffffff] (11.643422209270197,4.576451264833328) circle (2.5pt);
                                        \\draw [fill=ffffff] (6.82696330743721,4.55800256358029) circle (2.5pt);
                                    \\end{scriptsize}
                            \\end{tikzpicture}} }'''
                            %(latex(a), latex(b), latex(c), latex(r_sq)
                            ))

            # --- Ý a) TÂM VÀ BÁN KÍNH ---
            nb_da_1_d = '\\True Tâm mặt cầu là $I(%s;%s;%s)$ và bán kính $R=%s$' % (latex(a), latex(b), latex(c), latex(r))
            nb_da_1_s = 'Tâm mặt cầu là $I(%s;%s;%s)$ và bán kính $R=%s$' % (latex(a), latex(b), latex(c), latex(r_sq))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Dựa vào phương trình $(S)$, ta có tâm $I(%s;%s;%s)$ và bán kính $R=\\sqrt{%s}=%s$.''' % (latex(a), latex(b), latex(c), latex(r_sq), latex(r)))

            # --- Ý b) RANDOM 2 KIỂU CÂU HỎI ---
            loai_b = random.randint(1, 2)
            if loai_b == 1:
                # Kiểu 1: Đường thẳng vuông góc mặt sân
                th_da_1_d = '\\True Đường thẳng đi qua tâm mặt cầu $(S)$ và vuông góc với mặt sân có phương trình là $d: \\begin{cases} x=%s \\\\ y=%s \\\\ z=%s+t \\end{cases}$' % (latex(a), latex(b), latex(c))
                th_da_1_s = 'Đường thẳng đi qua tâm mặt cầu $(S)$ và vuông góc với mặt sân có phương trình là $d: \\begin{cases} x=%s+t \\\\ y=%s+t \\\\ z=%s \\end{cases}$' % (latex(a), latex(b), latex(c))
                loigiai_th_1 = ('''Đường thẳng $d$ vuông góc mặt sân ($z=0$) nên có VTCP $\\vec{u}=(0;0;1)$. Phương trình qua $I(%s;%s;%s)$ là $d: \\begin{cases} x=%s \\\\ y=%s \\\\ z=%s+t \\end{cases}$.''' % (latex(a), latex(b), latex(c), latex(a), latex(b), latex(c)))
            else:
                # Kiểu 2: Mặt phẳng song song mặt sân (Theo ảnh mới)
                # Phương trình đúng là z = c hay z - c = 0
                th_da_1_d = '\\True Mặt phẳng đi qua tâm mặt cầu $(S)$ và song song với mặt sân có phương trình là $z-%s=0$' % (latex(c))
                th_da_1_s = 'Mặt phẳng đi qua tâm mặt cầu $(S)$ và song song với mặt sân có phương trình là $z+%s=0$' % (latex(c))
                loigiai_th_1 = ('''Mặt phẳng song song với mặt sân ($z=0$) có dạng $z+D=0$. Vì mặt phẳng đi qua tâm $I(%s;%s;%s)$ nên $%s+D=0 \\Rightarrow D=-%s$. Vậy phương trình là $z-%s=0$.''' % (latex(a), latex(b), latex(c), latex(c), latex(c), latex(c)))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # --- Ý c) HÌNH CHIẾU H ---
            vd_da_1_d = '\\True Hình chiếu vuông góc của tâm $I$ trên sân là $H(%s;%s;0)$' % (latex(a), latex(b))
            vd_da_1_s = 'Hình chiếu vuông góc của tâm $I$ trên sân là $H(0;0;%s)$' % (latex(c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Hình chiếu của $I(%s;%s;%s)$ lên mặt phẳng $z=0$ là $H(%s;%s;0)$.''' % (latex(a), latex(b), latex(c), latex(a), latex(b)))

            # --- Ý d) KHOẢNG CÁCH MH ---
            mh_val = sqrt(r**2 - c**2)
            vdc_da_1_d = '\\True Khoảng cách $MH=%s$ m' % (latex(mh_val))
            vdc_da_1_s = 'Khoảng cách $MH=%s$ m' % (latex(r))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Ta có $IH = |z_I| = %s$, $IM = R = %s$. Suy ra $MH = \\sqrt{IM^2 - IH^2} = \\sqrt{%s^2 - %s^2} = %s$.''' % (latex(c), latex(r), latex(r), latex(c), latex(mh_val)))

            # --- HÀM ĐẾM ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # --- VÒNG LẶP ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán vào list để xáo trộn (Dù ở đây mỗi list chỉ có 1 phần tử đã chọn)
            list_nb_1 = [nb_sel]
            list_th_1 = [th_sel]
            list_vd_1 = [vd_sel]
            list_vdc_1 = [vdc_sel]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

