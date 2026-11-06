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


def bt_dang19_p3_b2_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ số ngẫu nhiên để tạo ra các đề khác nhau
                x_P_list = [2, 3, 4]
                z_A_list = [2.8, 3.1, 3.2]
                x_T_list = [4, 5, 6]
                y_T_list = [5, 6, 7]
                v_kmh_list = [144, 180, 216] # Tương ứng 40, 50, 60 m/s

                x_P = random.choice(x_P_list)
                z_A = random.choice(z_A_list)
                x_T = random.choice(x_T_list)
                y_T = random.choice(y_T_list)
                v_kmh = random.choice(v_kmh_list)

                # Đổi vận tốc ra m/s
                v_ms = v_kmh // 3.6 

                # Tính toán các vector và thành phần
                v_x = x_T - x_P
                v_y_mag = 24 - y_T
                z_A_frac = sp.Rational(int(z_A * 10), 10)

                # Hệ số tham số s
                s_frac = sp.Rational(y_T, v_y_mag)
                s_latex = latex(s_frac)

                # Tọa độ điểm K
                x_K_frac = x_T + s_frac * v_x
                z_K_frac = s_frac * z_A_frac

                # Tính quãng đường TK
                TK_sq = (x_K_frac - x_T)**2 + y_T**2 + z_K_frac**2
                TK_exact = sp.sqrt(TK_sq)
                TK_latex = latex(TK_exact)

                # Tính thời gian (chính xác và làm tròn)
                time_exact = TK_exact / int(v_ms)
                time_approx = float(time_exact)

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(time_approx)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_decimal).replace('.', ',')
                kq4 = float(kq_decimal)

                # Các đáp án trắc nghiệm sai (distractors)
                deltas = [0.05, -0.03, 0.12, -0.07, 0.08, -0.05]
                random.shuffle(deltas)
                s_options = []
                for d in deltas:
                    val = round(kq4 + d, 2)
                    if val > 0:
                        s_options.append('$%s$' % str(Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','))

                da = '$%s$' % kq
                das1 = s_options[0]
                das2 = s_options[1]
                das3 = s_options[2]

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Định dạng chuỗi cho các biến
                z_A_str = str(z_A).replace('.', ',')
                v_x_str = str(v_x)
                v_y_str = str(v_y_mag)

                sign_x = '+' if v_x >= 0 else '-'
                abs_vx = abs(v_x)

                # Code TikZ vẽ sân tennis 3D động khớp với các số liệu ngẫu nhiên
                tikz_cauhoi = ('''\\begin{center}
            \\begin{tikzpicture}[x={(-0.5cm,-0.4cm)}, y={(0.8cm,0cm)}, z={(0cm,0.8cm)}, scale=0.5, >=stealth, line width=1pt]
              \\pgfmathsetmacro{\\maxx}{10}
              \\pgfmathsetmacro{\\maxy}{24}
              \\fill[teal!20] (-2, -4, 0) -- (\\maxx+2, -4, 0) -- (\\maxx+2, \\maxy+4, 0) -- (-2, \\maxy+4, 0) -- cycle;
              \\draw[black, thick] (-2, -4, 0) -- (\\maxx+2, -4, 0) -- (\\maxx+2, \\maxy+4, 0) -- (-2, \\maxy+4, 0) -- cycle;
              \\fill[orange!30] (0,0,0) -- (\\maxx,0,0) -- (\\maxx,\\maxy,0) -- (0,\\maxy,0) -- cycle;
              \\draw[black, thick] (0,0,0) -- (\\maxx,0,0) -- (\\maxx,\\maxy,0) -- (0,\\maxy,0) -- cycle;
              \\draw[white, thick] (0,12,0) -- (\\maxx,12,0);
              \\fill[cyan!10, opacity=0.5] (0,12,0) -- (\\maxx,12,0) -- (\\maxx,12,1) -- (0,12,1) -- cycle;
              \\draw[red, thick] (-0.2,12,0) -- (-0.2,12,1.2);
              \\draw[red, thick] (\\maxx+0.2,12,0) -- (\\maxx+0.2,12,1.2);
              \\draw[white, thick] (0,12,1) -- (\\maxx,12,1);
              \\draw[->, black, thick] (0,0,0) -- (12,0,0) node[below] {$x$};
              \\draw[->, black, thick] (0,0,0) -- (0,28,0) node[below] {$y$};
              \\draw[->, black, thick] (0,0,0) -- (0,0,4) node[right] {$z$};
              \\draw[white, thick] (1.37, 0, 0) -- (1.37, \\maxy, 0);
              \\draw[white, thick] (8.63, 0, 0) -- (8.63, \\maxy, 0);
              \\draw[white, thick] (5, 5.5, 0) -- (5, 18.5, 0);
              \\draw[white, thick] (1.37, 5.5, 0) -- (8.63, 5.5, 0);
              \\draw[white, thick] (1.37, 18.5, 0) -- (8.63, 18.5, 0);
              \\coordinate (P) at (%s, 24, 0);
              \\coordinate (Pup) at (%s, 24, %s);
              \\coordinate (T) at (%s, %s, 0);
              \\coordinate (K) at (%s, 0, 0);
              \\coordinate (Kup) at (%s, 0, %s);
              \\draw[black, thin] (P) -- (Pup);
              \\fill[orange] (Pup) circle (2pt);
              \\node[below right] at (P) {$P$};
              \\fill[cyan] (T) circle (2pt) node[below] {$T$};
              \\draw[dashed, black, thin] (K) -- (Kup);
              \\fill[orange] (Kup) circle (2pt);
              \\node[left] at (K) {$K$};
              \\draw[blue, thick] (Pup) -- (T);
              \\draw[cyan, thick, dashed] (T) -- (Kup);
            \\end{tikzpicture}
            \\end{center}''' % (x_P, x_P, z_A, x_T, y_T, float(x_K_frac), float(x_K_frac), float(z_K_frac)))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Sân quần vợt được mô hình hóa lý tưởng, có chiều dài $24$ m và chiều rộng $10$ m. Các ô giao bóng dài $6$ m, rộng $5$ m và chiều cao của lưới là $1$ m. Giả sử, mọi cú đánh đều bay theo đường thẳng. Một vận động viên đứng ở vạch cuối sân tại điểm $P(%s; 24; 0)$ và đánh quả bóng với vận tốc $%s$ km/h ở độ cao $%s$ m sao cho bóng rơi đúng vào điểm $T(%s; %s; 0)$ của ô giao bóng. Sau khi chạm đất, bóng phản xạ theo góc $\\alpha$ (giữ nguyên vận tốc, không đổi hướng ngang) và tại vị trí $K$ trên vạch cuối sân bên kia đối thủ sẽ đánh trả. Thời gian đối thủ có để phản ứng được tính từ lúc bóng nảy lên khỏi mặt sân đến khi bóng tới vị trí đánh theo đơn vị giây? (Kết quả làm tròn đến hàng phần trăm).''' % (x_P, v_kmh, z_A_str, x_T, y_T)) + tikz_cauhoi

                # Nội dung lời giải
                loigiai = ('''Quỹ đạo từ $A(%s; 24; %s)$ đến $T(%s; %s; 0)$: $\\begin{cases} x = %s %s %st \\\\ y = 24 - %st \\quad (0 \\le t \\le 1) \\\\ z = %s - %st \\end{cases}$ (hướng $\\vec{v} = (%s; -%s; -%s)$)\\\\
            Sau nảy bóng thì phản xạ giữ nguyên vận tốc, không đổi hướng ngang\\\\
            Hướng mới $\\vec{v}' = (%s; -%s; %s)$ nên phương trình mới của quả bóng là $\\begin{cases} x = %s %s %ss \\\\ y = %s - %ss, (s > 0) \\\\ z = %ss \\end{cases}$\\\\
            Điểm $K$ trên vạch cuối sân bên kia thuộc mặt phẳng $y = 0$\\\\
            Suy ra: $%s - %ss = 0 \\Rightarrow s = %s \\Rightarrow K\\left(%s; 0; %s\\right)$\\\\
            Quãng đường $TK = \\sqrt{\\left(%s - %s\\right)^2 + %s^2 + \\left(%s\\right)^2} = %s$\\\\
            Vận tốc $%s \\text{ (km/h)} = %s \\text{ (m/s)}$ nên thời gian đối thủ có để phản ứng: $t = \\frac{TK}{%s} \\approx %s \\text{ (giây)}$.''' % (
                    x_P, z_A_str, x_T, y_T, 
                    x_P, sign_x, abs_vx, v_y_str, z_A_str, z_A_str, v_x_str, v_y_str, z_A_str,
                    v_x_str, v_y_str, z_A_str, x_T, sign_x, abs_vx, y_T, v_y_str, z_A_str,
                    y_T, v_y_str, s_latex, latex(x_K_frac), latex(z_K_frac),
                    latex(x_K_frac), x_T, y_T, latex(z_K_frac), TK_latex,
                    v_kmh, int(v_ms), int(v_ms), kq
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

