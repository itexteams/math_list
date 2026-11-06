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


def bt_dang43_p3_b3_c1_ds12(self):
    # Hàm định dạng số hiển thị trong LaTeX (chuyển dấu chấm thành dấu phẩy)
    def fmt(num):
        if isinstance(num, (int, float, Decimal)):
            if float(num).is_integer():
                return str(int(num))
            else:
                s = f"{float(num):g}"
                return s.replace('.', ',')
        return str(num).replace('.', ',')
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Vòng lặp đảm bảo sinh số ngẫu nhiên nhưng kết quả T (phút) luôn là số nguyên đẹp
        while True:
            A_val = random.choice([6, 8, 10, 12, 15, 20])
            B_val = random.choice([2, 3, 4, 5, 6])
            if B_val >= A_val:
                continue
            C_val = random.choice([1, 2])
            M_val = random.choice([4, 5, 6, 8, 10])
            N_val = random.choice([1, 2, 3, 4])
            p_val = random.choice([75, 80, 85, 90, 95])

            # Ngưỡng K = (M * A) / (A + N)
            K_rat = Rational(M_val * A_val, A_val + N_val)

            # Tốc độ mục tiêu V_target = (p / 100) * K
            V_target = Rational(p_val, 100) * K_rat

            # Giải V(S) = V_target => M*S / (S + N) = V_target => S*(M - V_target) = N * V_target
            if M_val <= V_target:
                continue
            S_rat = (N_val * V_target) / (M_val - V_target)

            # Nồng độ ban đầu S(0) = B / C. Cần S_rat > S(0)
            if S_rat <= Rational(B_val, C_val) or S_rat >= A_val:
                continue

            # Giải S(t) = S => (A*t + B) / (t + C) = S => t*(A - S) = S*C - B
            t_rat = (S_rat * C_val - B_val) / (A_val - S_rat)

            # Đổi t (giờ) ra T (phút)
            T_rat = t_rat * 60

            # Kiểm tra T_rat là số nguyên dương đẹp
            if T_rat.q == 1 and T_rat > 0:
                T_val = int(T_rat)
                if 5 <= T_val <= 120:
                    break

        # Tính toán các đại lượng hỗ trợ cho lời giải chi tiết
        K_float = float(K_rat)
        V_target_float = float(V_target)
        S_float = float(S_rat)
        t_float = float(t_rat)

        A_str = fmt(A_val)
        B_str = fmt(B_val)
        C_str = fmt(C_val)
        M_str = fmt(M_val)
        N_str = fmt(N_val)
        p_str = fmt(p_val)

        K_str = fmt(K_rat)
        V_target_str = fmt(V_target)
        S_str = fmt(S_rat)
        t_str = fmt(t_rat)
        T_str = fmt(T_val)

        # Đáp án đúng
        kq = T_str
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # Tạo các phương án sai (không trùng nhau và không trùng đáp án đúng)
        wrong_set = set()
        for offset in [-10, -5, 5, 10, 15, 20, 30]:
            w = T_val + offset
            if w > 0 and w != T_val:
                wrong_set.add(w)

        if int(round(t_float)) > 0 and int(round(t_float)) != T_val:
            wrong_set.add(int(round(t_float)))

        s = ['$%s$' % (fmt(v)) for v in wrong_set]
        random.shuffle(s)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{Một quần thể vi khuẩn được nuôi cấy trong phòng thí nghiệm. Nồng độ dinh dưỡng $S$ (đơn vị: mg/l) thay đổi theo thời gian $t$ giờ ($t \\ge 0$) được mô hình hóa bởi hàm số: $S(t) = \\frac{%st + %s}{t + %s}$. Biết tốc độ sinh trưởng $V$ của vi khuẩn phụ thuộc vào nồng độ dinh dưỡng theo hàm số $V(S) = \\frac{%sS}{S + %s}$. Khi thời gian $t$ kéo dài, tốc độ sinh trưởng $V$ tăng dần và ổn định quanh một ngưỡng $K$ nhất định. Hỏi sau bao nhiêu phút thì tốc độ sinh trưởng của vi khuẩn đạt $%s\\%%$ ngưỡng $K$?}
                         {\\begin{tikzpicture}[line cap=round,line join=round, scale=0.5]
                         	\\definecolor{microRed}{RGB}{215,55,78}
                         	\\definecolor{microGreen}{RGB}{119,163,56}
                         	\\definecolor{microTeal}{RGB}{39,169,158}
                         	\\definecolor{microPurple}{RGB}{151,91,165}
                         	\\definecolor{microLime}{RGB}{150,190,67}
                         	\\newcommand{\\spikyvirus}[2]{
                         		\\begin{scope}[shift={#1},scale=#2]
                         			\\foreach \\a in {0,30,...,330}{
                         				\\draw[draw=microRed,line width=1.2pt] (\\a:0.48) -- (\\a:0.76);
                         				\\fill[microRed] (\\a:0.82) circle (0.075);
                         			}
                         			\\fill[microRed!88!black] (0,0) circle (0.52);
                         			\\fill[microRed!55!white] (0,0) circle (0.43);
                         			\\foreach \\p in {(-.18,.17),(.16,.20),(.22,-.13),(-.16,-.19),(0,.02)}
                         			\\fill[microRed!85!black] \\p circle (0.075);
                         			\\foreach \\p in {(-.31,.02),(.02,.31),(.31,.03),(.03,-.31)}
                         			\\fill[white,opacity=.72] \\p circle (0.035);
                         		\\end{scope}                      	}
                         	\\spikyvirus{(0,0)}{1}
                         	\\begin{scope}[shift={(3.1,0)},rotate=25]
                         		\\foreach \\y in {-0.72,-0.48,...,0.72}{
                         			\\draw[microGreen!85!black,line width=1pt] (-.22,\\y) -- (-.52,\\y-.14);
                         			\\draw[microGreen!85!black,line width=1pt] (.22,\\y) -- (.52,\\y+.14);  }
                         		\\draw[fill=microGreen!78!white,draw=microGreen!70!black,line width=1pt,rounded corners=0.25cm]
                         		(-.25,-.88) rectangle (.25,.88);
                         		\\foreach \\y in {-.62,-.31,0,.31,.62}
                         		\\draw[microGreen!75!black,line width=1.2pt] (-.22,\\y) .. controls (0,\\y-.16) .. (.22,\\y);
                         		\\foreach \\p in {(-.08,-.48),(.09,-.08),(-.08,.35),(.08,.65)}
                         		\\fill[microGreen!70!black] \\p circle (0.045);
                         	\\end{scope}
                         	\\begin{scope}[shift={(6.25,0)}]
                         		\\foreach \\x/\\y/\\r/\\c in {-.45/.16/.43/microPurple,.54/.30/.42/microTeal,.19/-.43/.34/microLime}
                         		{\\fill[\\c!70!white] (\\x,\\y) circle (\\r);\\draw[\\c!80!black,line width=.8pt] (\\x,\\y) circle (\\r);}
                         		\\foreach \\x/\\y in {-.58/.22,-.37/.04,-.29/.29,.43/.42,.65/.22,.52/.09,.10/-.39,.27/-.50}
                         		\\fill[white,opacity=.55] (\\x,\\y) circle (.045);
                         	\\end{scope}
                         	\\spikyvirus{(-.52,-2.85)}{.48}
                         	\\spikyvirus{(.64,-2.55)}{.55}
                         	\\spikyvirus{(.28,-3.45)}{.38}
                         	\\begin{scope}[shift={(3.1,-2.85)},rotate=-18]
                         		\\fill[microLime!72!white,draw=microGreen!80!black,line width=1pt]
                         		plot[smooth cycle] coordinates {(-.43,-.68) (-.10,-.82) (.22,-.61) (.37,-.27) (.22,.05) (.39,.41) (.12,.76) (-.24,.68) (-.38,.36) (-.19,.08) (-.43,-.19)};
                         		\\draw[microGreen!70!black,line width=2pt] (-.12,-.55) .. controls (.30,-.25) and (-.28,.06) .. (.12,.43) .. controls (.29,.57) .. (.02,.63);
                         		\\foreach \\x/\\y in {-.19/-.47,.10/-.30,.12/.08,-.08/.27,.16/.50}
                         		\\fill[microGreen!65!black] (\\x,\\y) circle (.055);
                         	\\end{scope}
                         	\\begin{scope}[shift={(6.25,-2.85)}]
                         		\\foreach \\x/\\y/\\r in {-.55/.43/.22,-.04/.60/.20,.48/.52/.18,.78/.16/.16,-.61/-.05/.19,-.12/.12/.22,.34/.12/.19,.69/-.32/.18,-.53/-.49/.20,-.05/-.43/.22,.40/-.62/.18,.05/-.83/.13}
                         		{\\fill[microTeal!68!white] (\\x,\\y) circle (\\r);\\draw[microTeal!80!black,line width=.8pt] (\\x,\\y) circle (\\r);\\fill[white,opacity=.65] (\\x-.04,\\y+.05) circle (.045);}
                         	\\end{scope}
                         	\\begin{scope}[shift={(.05,-5.72)},rotate=-35]
                         		\\draw[microTeal!75!black,line width=1pt] (-.48,.02) .. controls (-.78,.36) and (-.95,.20) .. (-1.05,.48);
                         		\\draw[microTeal!75!black,line width=1pt] (.48,.02) .. controls (.80,-.30) and (.91,-.08) .. (1.08,-.30);
                         		\\draw[fill=microTeal!45!white,draw=microTeal!80!black,line width=1pt] (-.53,0) ellipse (.58 and .27);
                         		\\foreach \\x in {-.80,-.55,-.30,-.05,.20}
                         		\\draw[microTeal!70!black,line width=.8pt] (\\x,-.22) -- (\\x-.12,-.37);
                         		\\foreach \\x/\\y in {-.70/.04,-.44/-.04,-.18/.05,.08/-.05,.30/.04}
                         		\\fill[microTeal!70!black] (\\x,\\y) circle (.055);
                         	\\end{scope}
                         	\\begin{scope}[shift={(1.05,-6.18)},rotate=18,scale=.72]
                         		\\draw[microTeal!75!black,line width=1pt] (-.45,.05) .. controls (-.75,.42) and (-.90,.24) .. (-1.02,.50);
                         		\\draw[microTeal!75!black,line width=1pt] (.45,.02) .. controls (.76,-.28) and (.91,-.06) .. (1.04,-.25);
                         		\\draw[fill=microTeal!45!white,draw=microTeal!80!black,line width=1pt] (0,0) ellipse (.58 and .27);
                         		\\foreach \\x/\\y in {-.35/.04,-.10/-.04,.15/.05,.36/-.04}
                         		\\fill[microTeal!70!black] (\\x,\\y) circle (.06);
                         	\\end{scope}
                         	\\begin{scope}[shift={(3.25,-5.72)},rotate=28]
                         		\\foreach \\a in {155,170,...,385}
                         		\\draw[microTeal!65!black,line width=.8pt] (\\a:.70) -- (\\a:1.00);
                         		\\fill[microTeal!78!black] plot[smooth cycle] coordinates {(-.46,-.22) (-.32,-.50) (.02,-.42) (.31,-.15) (.48,.20) (.35,.43) (.02,.30) (-.25,.47) (-.48,.20)};
                         		\\foreach \\x/\\y in {-.25/-.17,-.02/-.20,.20/-.08,.28/.17,.05/.14,-.20/.23}
                         		\\fill[microTeal!38!white] (\\x,\\y) circle (.07);
                         		\\draw[microTeal!75!black,line width=1pt] (.20,.35) .. controls (.55,.68) and (.65,.65) .. (.82,.85);
                         	\\end{scope}
                         	\\begin{scope}[shift={(6.25,-5.72)}]
                         		\\foreach \\a in {0,15,...,345}
                         		\\draw[microGreen!65!white,line width=1pt] (\\a:.47) -- (\\a:.88);
                         		\\fill[microGreen!24!white,draw=microGreen!60!white,line width=1pt] (0,0) ellipse (.43 and .56);
                         		\\foreach \\x/\\y in {-.18/.31,.06/.34,.18/.17,-.16/.08,.08/.02,-.20/-.13,.13/-.21,-.02/-.40}
                         		\\fill[microTeal!65!black] (\\x,\\y) circle (.055);
                         	\\end{scope}
                         \\end{tikzpicture}}'''
                         % (A_str, B_str, C_str, M_str, N_str, p_str))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Trộn các đáp án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết
        loigiai = ('''Khi thời gian $t$ kéo dài ($t \\rightarrow +\\infty$), ta có: \\\\
                 $\\lim_{t \\rightarrow +\\infty} S(t) = \\lim_{t \\rightarrow +\\infty} \\frac{%st + %s}{t + %s} = %s$ (mg/l). \\\\
                 Khi đó, tốc độ sinh trưởng $V$ tiệm cận đến ngưỡng $K$: \\\\
                 $K = \\lim_{S \\rightarrow %s} V(S) = \\lim_{S \\rightarrow %s} \\frac{%sS}{S + %s} = \\frac{%s \\cdot %s}{%s + %s} = %s$. \\\\
                 Theo đề bài, tốc độ sinh trưởng của vi khuẩn đạt $%s\\%%$ ngưỡng $K$, tức là: \\\\
                 $V(S) = %s\\%% \\cdot %s = %s$. \\\\
                 Thay vào công thức $V(S) = \\frac{%sS}{S + %s}$, ta được: \\\\
                 $\\frac{%sS}{S + %s} = %s \\Leftrightarrow S = %s$ (mg/l). \\\\
                 Thay $S = %s$ vào công thức $S(t) = \\frac{%st + %s}{t + %s}$, ta có: \\\\
                 $\\frac{%st + %s}{t + %s} = %s \\Leftrightarrow t = %s$ (giờ). \\\\
                 Đổi ra phút: $%s \\text{ giờ} = %s \\cdot 60 = %s$ phút. \\\\
                 Vậy sau $%s$ phút thì tốc độ sinh trưởng của vi khuẩn đạt $%s\\%%$ ngưỡng $K$.'''
                 % (A_str, B_str, C_str, A_str,
                    A_str, A_str, M_str, N_str, M_str, A_str, A_str, N_str, K_str,
                    p_str, p_str, K_str, V_target_str,
                    M_str, N_str,
                    M_str, N_str, V_target_str, S_str,
                    S_str, A_str, B_str, C_str,
                    A_str, B_str, C_str, S_str, t_str,
                    t_str, t_str, T_str,
                    T_str, p_str))
    dapan='\\shortans[0]{$%s$}\n'%(T_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

