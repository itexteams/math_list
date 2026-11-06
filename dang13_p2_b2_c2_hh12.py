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


def bt_dang13_p2_b2_c2_hh12(self):
            # Khai báo biến
            # Random bộ dữ liệu đầu vào để đảm bảo số liệu tính toán không quá xấu
            datasets = [
                {'xG': 3, 'y0': 4, 'zG': 2, 'c': 1, 'zL1': 5, 'zL2': 4, 'pc_true': 200, 'pc_false': 220},
                {'xG': 2, 'y0': 4, 'zG': 2, 'c': 1, 'zL1': 6, 'zL2': 5, 'pc_true': 80, 'pc_false': 100},
                {'xG': 3, 'y0': 6, 'zG': 3, 'c': 1, 'zL1': 6, 'zL2': 5, 'pc_true': 220, 'pc_false': 250},
            ]
            data = random.choice(datasets)
            xG = data['xG']
            y0 = data['y0']
            zG = data['zG']
            c = data['c']
            zL1 = data['zL1']
            zL2 = data['zL2']
            pc_t = data['pc_true']
            pc_f = data['pc_false']

            a_side = 2 * c

            # Tính tọa độ các đỉnh của cửa sổ ABCD
            xA, yA, zA = xG + c, y0, zG - c
            xB, yB, zB = xG - c, y0, zG - c
            xC, yC, zC = xG - c, y0, zG + c
            xD, yD, zD = xG + c, y0, zG + c

            # Tính toán các thông số chuẩn xác bằng sympy
            t_G = Rational(zL1, zL1 - zG)
            yG_prime = y0 * t_G

            # Mệnh đề c:
            z_AB = zG - c
            z_CD = zG + c
            y1 = y0 * Rational(zL1, zL1 - z_AB)
            y2 = y0 * Rational(zL1, zL1 - z_CD)
            w1 = a_side * Rational(zL1, zL1 - z_AB)
            w2 = a_side * Rational(zL1, zL1 - z_CD)
            h1 = y2 - y1
            S1 = (w1 + w2) * h1 / 2

            # Mệnh đề d:
            t_A_prime2 = Rational(zL2, zL2 - z_AB)
            t_C_prime2 = Rational(zL2, zL2 - z_CD)

            xA_prime2 = xG + (xA - xG) * t_A_prime2
            xB_prime2 = xG + (xB - xG) * t_A_prime2
            xC_prime2 = xG + (xC - xG) * t_C_prime2
            xD_prime2 = xG + (xD - xG) * t_C_prime2

            yA_prime2 = y0 * t_A_prime2
            yC_prime2 = y0 * t_C_prime2

            w1_prime = abs(xB_prime2 - xA_prime2)
            w2_prime = abs(xD_prime2 - xC_prime2)

            h2 = yC_prime2 - yA_prime2
            S2 = (w1_prime + w2_prime) * h2 / 2

            percent_val_exact = (S2 - S1) / S1 * 100
            percent_exact_f = float(percent_val_exact)
            if percent_exact_f.is_integer():
                cmp_sign = "="
                percent_str = str(int(percent_exact_f))
            else:
                cmp_sign = "\\approx"
                percent_str = str(round(percent_exact_f))

            # Tính tọa độ bóng lần chiếu 1 (dùng cho việc vẽ hình)
            t_A_prime1 = Rational(zL1, zL1 - zA)
            t_C_prime1 = Rational(zL1, zL1 - zC)
            xA_prime1 = xG + (xA - xG) * t_A_prime1
            xB_prime1 = xG + (xB - xG) * t_A_prime1
            xC_prime1 = xG + (xC - xG) * t_C_prime1
            xD_prime1 = xG + (xD - xG) * t_C_prime1
            yA_prime1 = y0 * t_A_prime1
            yC_prime1 = y0 * t_C_prime1

            # Hàm format số liệu đẹp
            def fmt(val):
                if isinstance(val, sp.Rational):
                    if val.q == 1: return str(val.p)
                    if val.q in [2, 4, 5, 8, 10, 16, 20, 25]:
                        return str(float(val)).replace('.', ',')
                try:
                    f_val = float(val)
                    if f_val.is_integer(): return str(int(f_val))
                except: pass
                return sp.latex(val).replace('.', ',')

            def fmt_vec(vx, vy, vz):
                return f"({fmt(vx)}; {fmt(vy)}; {fmt(vz)})"

            def linear_term(a, b, var='t'):
                if b == 0: return fmt(a)
                abs_b = abs(b)
                b_str = "" if abs_b == 1 else fmt(abs_b)
                if a == 0:
                    sign = "-" if b < 0 else ""
                    return f"{sign}{b_str}{var}"
                sign = "+" if b > 0 else "-"
                return f"{fmt(a)} {sign} {b_str}{var}"

            tikz_str = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[x={{(-0.5cm,-0.5cm)}}, y={{(1cm,0cm)}}, z={{(0cm,1cm)}}, font=\\footnotesize, line width=1pt,scale=0.6]
            \\draw[->] (0,0,0) -- ({float(xG+4)},0,0) node[above] {{$x$}};
            \\draw[->] (0,0,0) -- (0,{float(yC_prime1+2)},0) node[above] {{$y$}};
            \\draw[->] (0,0,0) -- (0,0,{float(zL1+1)}) node[right] {{$z$}};
            \\node[left] at (0,0,0) {{$O$}};
            \\draw[dashed, thick] (0,0,0) -- (0,{float(y0)},0);
            \\fill[orange] ({float(xG)},0,{float(zL1)}) circle (2pt) node[above, black] {{$L$}};
            \\draw[cyan, fill=cyan!20, opacity=0.8] ({float(xG+3)},{float(y0)},0) -- ({float(xG-4)},{float(y0)},0) -- ({float(xG-4)},{float(y0)},{float(zG+c+1.5)}) -- ({float(xG+3)},{float(y0)},{float(zG+c+1.5)}) -- cycle;
            \\draw[blue, thick, fill=white] ({float(xA)},{float(y0)},{float(zA)}) node[left, black] {{$A$}} -- ({float(xB)},{float(y0)},{float(zB)}) node[right, black] {{$B$}} -- ({float(xC)},{float(y0)},{float(zC)}) node[above, black] {{$C$}} -- ({float(xD)},{float(y0)},{float(zD)}) node[left, black] {{$D$}} -- cycle;
            \\draw[orange, thick, fill=orange!20, opacity=0.8] ({float(xA_prime1)}, {float(yA_prime1)}, 0) node[left, black] {{$A'$}} -- ({float(xB_prime1)}, {float(yA_prime1)}, 0) node[right, black] {{$B'$}} -- ({float(xC_prime1)}, {float(yC_prime1)}, 0) node[right, black] {{$C'$}} -- ({float(xD_prime1)}, {float(yC_prime1)}, 0) node[left, black] {{$D'$}} -- cycle;
            \\draw[dashed, orange] ({float(xG)},0,{float(zL1)}) -- ({float(xA_prime1)}, {float(yA_prime1)}, 0);
            \\draw[dashed, orange] ({float(xG)},0,{float(zL1)}) -- ({float(xB_prime1)}, {float(yA_prime1)}, 0);
            \\draw[dashed, orange] ({float(xG)},0,{float(zL1)}) -- ({float(xC_prime1)}, {float(yC_prime1)}, 0);
            \\draw[dashed, orange] ({float(xG)},0,{float(zL1)}) -- ({float(xD_prime1)}, {float(yC_prime1)}, 0);
            \\end{{tikzpicture}}
            \\end{{center}}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$ mới mặt sàn là mặt phẳng $Oxy$, cửa sổ hình vuông $ABCD$ cạnh bằng %s m nằm trong mặt phẳng $y = %s$ và song song với $(Oxz)$. Tâm cửa sổ là điểm $G(%s;%s;%s)$ và các cạnh song song với các trục tọa độ. Người ta đặt một nguồn sáng tại điểm $L(%s;0;%s)$ chiếu sáng qua cửa sổ và tạo bóng trên mặt sàn.
            %s''' % (fmt(a_side), fmt(y0), fmt(xG), fmt(y0), fmt(zG), fmt(xG), fmt(zL1), tikz_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình mặt phẳng chứa cửa sổ là $y - %s = 0$' % (fmt(y0))
            nb_da_1_s = 'Phương trình mặt phẳng chứa cửa sổ là $y - %s = 0$' % (fmt(y0+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Theo đề bài thì cửa sổ hình vuông $ABCD$ cạnh bằng %s m nằm trong mặt phẳng $y = %s$. \\\\
            Suy ra phương trình mặt phẳng chứa cửa sổ là $y - %s = 0$.''' % (fmt(a_side), fmt(y0), fmt(y0)))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tọa độ tâm của bóng cửa sổ trên mặt sàn là $G\'%s$' % (fmt_vec(xG, yG_prime, 0))
            th_da_1_s = 'Tọa độ tâm của bóng cửa sổ trên mặt sàn là $G\'%s$' % (fmt_vec(xG, yG_prime+1, 0))
            list_th_da_1=[th_da_1_d,th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $G'$ là giao điểm của đường thẳng $LG$ lên mặt phẳng $(Oxy)$ nên $\\overrightarrow{LG} = (0; %s; %s)$. \\\\
            Phương trình đường thẳng $LG$: $\\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases} (t \\in \\mathbb{R})$. \\\\
            Tại giao điểm với mặt sàn $(z=0) \\Leftrightarrow %s = 0 \\Rightarrow t = %s$ nên $G'%s$.'''
            % (fmt(y0), fmt(zG-zL1),
               fmt(xG), linear_term(0, y0), linear_term(zL1, zG-zL1),
               linear_term(zL1, zG-zL1), fmt(t_G), fmt_vec(xG, yG_prime, 0)))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Diện tích bóng của cửa sổ trên mặt sàn bằng %s m$^2$' % (fmt(S1))
            vd_da_1_s = 'Diện tích bóng của cửa sổ trên mặt sàn bằng %s m$^2$' % (fmt(S1+10))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $M(x_M; %s; z_M)$ là một điểm thuộc cửa sổ. \\\\
            Phương trình đường thẳng $LM$: $\\frac{x-%s}{x_M-%s} = \\frac{y-0}{%s-0} = \\frac{z-%s}{z_M-%s}$. \\\\
            Tại mặt sàn $(z=0)$ ta có tỉ lệ: $\\frac{y}{%s} = \\frac{-%s}{z_M-%s} \\Rightarrow y = \\frac{-%s}{z_M-%s}$. \\\\
            Với cạnh $AB$: $z_M = %s \\Rightarrow y = %s$ thì chiều rộng bóng: $r_1 = \\frac{%s}{%s-%s} \\cdot %s = %s$ (m). \\\\
            Với cạnh $CD$: $z_M = %s \\Rightarrow y = %s$ thì chiều rộng bóng: $r_2 = \\frac{%s}{%s-%s} \\cdot %s = %s$ (m). \\\\
            Chiều cao bóng: $h = %s - %s = %s$ (m) nên $S_{A'B'C'D'} = \\frac{%s + %s}{2} \\cdot %s = %s$ (m$^2$).'''
            % (fmt(y0),
               fmt(xG), fmt(xG), fmt(y0), fmt(zL1), fmt(zL1),
               fmt(y0), fmt(zL1), fmt(zL1), fmt(zL1*y0), fmt(zL1),
               fmt(zA), fmt(y1), fmt(zL1), fmt(zL1), fmt(zA), fmt(a_side), fmt(w1),
               fmt(zC), fmt(y2), fmt(zL1), fmt(zL1), fmt(zC), fmt(a_side), fmt(w2),
               fmt(y2), fmt(y1), fmt(h1), fmt(w1), fmt(w2), fmt(h1), fmt(S1)))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu hạ thấp nguồn sáng $L$ xuống vị trí mới là $L\'%s$ thì diện tích bóng mới sẽ tăng thêm hơn %s\\%% so với diện tích bóng ban đầu' % (fmt_vec(xG, 0, zL2), pc_t)
            vdc_da_1_s = 'Nếu hạ thấp nguồn sáng $L$ xuống vị trí mới là $L\'%s$ thì diện tích bóng mới sẽ tăng thêm hơn %s\\%% so với diện tích bóng ban đầu' % (fmt_vec(xG, 0, zL2), pc_f)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Vectơ $\\overrightarrow{L'A} = (%s; %s; %s)$ nên phương trình đường thẳng $L'A$: $\\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases} (t \\in \\mathbb{R})$. \\\\
            $L'A \\cap (Oxy) \\Leftrightarrow %s = 0 \\Rightarrow t = %s$. Mà $A'' \\in L'A \\Rightarrow A''%s$. \\\\
            Tương tự cho $B%s$, ta tìm được $B''%s$ suy ra $A''B'' = \\sqrt{(%s - %s)^2} = %s$ (m). \\\\
            Vectơ $\\overrightarrow{L'C} = (%s; %s; %s)$ nên phương trình đường thẳng $L'C$: $\\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases} (t \\in \\mathbb{R})$. \\\\
            Ta có: $L'C \\cap (Oxy) \\Leftrightarrow %s = 0 \\Rightarrow t = %s$. Mà $C'' \\in L'C \\Rightarrow C''%s$. \\\\
            Tương tự cho $D%s$, ta tìm được $D''%s$ nên $C''D'' = \\sqrt{(%s - %s)^2} = %s$ (m). \\\\
            Chiều cao hình thang cân $A''B''C''D''$: $h = |y_{D''} - y_{A''}| = %s - %s = %s$ (m) nên $S_{A''B''C''D''} = \\frac{%s + %s}{2} \\cdot %s = %s$ (m$^2$). \\\\
            Phần trăm tăng thêm : $\\%%T = \\frac{S_{A''B''C''D''} - S_{A'B'C'D'}}{S_{A'B'C'D'}} \\cdot 100 = \\frac{%s - %s}{%s} \\cdot 100 %s %s > %s$.'''
            % (fmt(xA-xG), fmt(y0), fmt(zA-zL2), linear_term(xG, xA-xG), linear_term(0, y0), linear_term(zL2, zA-zL2),
               linear_term(zL2, zA-zL2), fmt(t_A_prime2), fmt_vec(xA_prime2, yA_prime2, 0),
               fmt_vec(xB, y0, zB), fmt_vec(xB_prime2, yA_prime2, 0), fmt(xB_prime2), fmt(xA_prime2), fmt(w1_prime),
               fmt(xC-xG), fmt(y0), fmt(zC-zL2), linear_term(xG, xC-xG), linear_term(0, y0), linear_term(zL2, zC-zL2),
               linear_term(zL2, zC-zL2), fmt(t_C_prime2), fmt_vec(xC_prime2, yC_prime2, 0),
               fmt_vec(xD, y0, zD), fmt_vec(xD_prime2, yC_prime2, 0), fmt(xD_prime2), fmt(xC_prime2), fmt(w2_prime),
               fmt(yC_prime2), fmt(yA_prime2), fmt(h2), fmt(w1_prime), fmt(w2_prime), fmt(h2), fmt(S2),
               fmt(S2), fmt(S1), fmt(S1), cmp_sign, percent_str, pc_t))

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content 

