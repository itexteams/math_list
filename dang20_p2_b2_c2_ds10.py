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


def bt_dang20_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên các tham số bài toán
            while True:
                # Chọn tọa độ giao điểm B(x0, y0) làm điểm tối ưu
                x0 = random.choice([5, 10])
                y0 = random.choice([2, 4, 6])

                # Giá thuê xe A và xe B (triệu đồng)
                c_A = random.choice([4, 5])
                c_B = random.choice([3, 4])

                if c_A <= c_B:
                    continue

                # Số người N và số tấn hàng H
                N = 20 * x0 + 10 * y0
                H_val = 0.6 * x0 + 1.5 * y0

                # Đảm bảo H là số nguyên để bài toán đẹp
                if H_val != int(H_val):
                    continue

                H = int(H_val)
                str_H = "%s" % H

                # Hệ số rút gọn của bất phương trình:
                # 20x + 10y >= N  <=>  2x + y >= k1
                k1 = 2 * x0 + y0

                # 0.6x + 1.5y >= H <=> 6x + 15y >= 10H <=> 2x + 5y >= k2
                k2 = 2 * x0 + 5 * y0

                # Số lượng xe tối đa sẵn có
                max_A = x0 + random.choice([5, 6, 7])
                max_B = y0 + random.choice([4, 5, 6])

                # Chi phí thấp nhất
                min_cost = c_A * x0 + c_B * y0
                fake_cost = min_cost - random.choice([2, 4])

                break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty TNHH trong một đợt quảng cáo và bán hàng khuyến mại hàng hóa cần thuê xe để chở %s người và %s tấn hàng. Nơi thuê chỉ có hai loại xe A và B. Trong đó xe loại A có %s chiếc, xe loại B có %s chiếc. Một chiếc xe loại A cho thuê với giá %s triệu, loại B giá %s triệu. Biết rằng xe A chỉ chở tối đa 20 người và 0,6 tấn hàng; xe B chở tối đa 10 người và 1,5 tấn hàng. Gọi $x, y$ lần lượt là số xe loại A và loại B mà công ty thuê.''' % (N, str_H, max_A, max_B, c_A, c_B))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Số tiền thuê xe là $%sx + %sy$' % (c_A, c_B)
            nb_da_1_s = 'Số tiền thuê xe là $%sx + %sy$' % (c_B, c_A)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True $2x + y \\ge %s$' % k1
            th_da_1_s = '$2x + y < %s$' % k1
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True $2x + 5y \\ge %s$' % k2
            vd_da_1_s = '$2x + 5y < %s$' % k2
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Số tiền thuê xe thấp nhất là %s triệu' % min_cost
            vdc_da_1_s = 'Số tiền thuê xe thấp nhất là %s triệu' % fake_cost
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

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

            # Lời giải Nhận biết
            if '\\True' in nb_da_1:
                loigiai_nb_1 = ('Số tiền thuê $x$ xe loại A là $%sx$ (triệu đồng), số tiền thuê $y$ xe loại B là $%sy$ (triệu đồng). \\\\ Tổng số tiền thuê xe là $%sx + %sy$ (triệu đồng). Do đó phát biểu trên là đúng.' % (c_A, c_B, c_A, c_B))
            else:
                loigiai_nb_1 = ('Số tiền thuê $x$ xe loại A là $%sx$ (triệu đồng), số tiền thuê $y$ xe loại B là $%sy$ (triệu đồng). \\\\ Tổng số tiền thuê xe là $%sx + %sy$ (triệu đồng). Do đó phát biểu trên là sai.' % (c_A, c_B, c_A, c_B))

            # Lời giải Thông hiểu
            if '\\True' in th_da_1:
                loigiai_th_1 = ('Số người $x$ xe loại A và $y$ xe loại B chở được là $20x + 10y$ (người). \\\\ Vì công ty cần chở ít nhất %s người nên ta có bất phương trình $20x + 10y \\ge %s \\Leftrightarrow  2x + y \\ge %s$. Do đó phát biểu trên là đúng.' % (N, N, k1))
            else:
                loigiai_th_1 = ('Số người $x$ xe loại A và $y$ xe loại B chở được là $20x + 10y$ (người). \\\\ Vì công ty cần chở ít nhất %s người nên ta có bất phương trình $20x + 10y \\ge %s \\Leftrightarrow  2x + y \\ge %s$. Do đó phát biểu trên là sai.' % (N, N, k1))

            # Lời giải Vận dụng
            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('Số tấn hàng $x$ xe loại A và $y$ xe loại B chở được là $0,6x + 1,5y$ (tấn). \\\\ Vì công ty cần chở ít nhất %s tấn hàng nên ta có bất phương trình $0,6x + 1,5y \\ge %s \\Leftrightarrow  2x + 5y \\ge %s$. Do đó phát biểu trên là đúng.' % (str_H, str_H, k2))
            else:
                loigiai_vd_1 = ('Số tấn hàng $x$ xe loại A và $y$ xe loại B chở được là $0,6x + 1,5y$ (tấn). \\\\ Vì công ty cần chở ít nhất %s tấn hàng nên ta có bất phương trình $0,6x + 1,5y \\ge %s \\Leftrightarrow  2x + 5y \\ge %s$. Do đó phát biểu trên là sai.' % (str_H, str_H, k2))

            # Tính toán tọa độ và tỉ lệ thu phóng cho hình vẽ TikZ
            yA = k1
            xA = 0

            xB = x0
            yB = y0

            xC = k2 / 2.0
            yC = 0

            max_coord = max(yA, xC)
            S = max_coord / 3.0  # Tỉ lệ quy về khoảng ~3 đơn vị độ dài trong khung clip

            yA_p = yA / S
            xB_p = xB / S
            yB_p = yB / S
            xC_p = xC / S

            # Điểm giao của 2 đường thẳng d1, d2 với ranh giới khung clip x=-2 và x=4
            l1_y_m2 = (k1/S) - 2 * (-2)
            l1_y_4 = (k1/S) - 2 * (4)

            l2_y_m2 = ((k2/S) - 2 * (-2)) / 5.0
            l2_y_4 = ((k2/S) - 2 * (4)) / 5.0

            # Lời giải Vận dụng cao
            val_A = c_B * k1
            val_B = min_cost
            val_C = c_A * xC
            val_C_str = "%g" % val_C if val_C == int(val_C) else "%s" % latex(Rational(int(k2 * c_A), 2))
            xC_str = "%g" % xC if xC == int(xC) else "%s" % latex(Rational(k2, 2))

            if '\\True' in vdc_da_1:
                eval_vdc = "Do đó phát biểu trên là đúng."
            else:
                eval_vdc = "Do đó phát biểu trên là sai."

            loigiai_vdc_1 = ('''Số tiền thuê xe là $T(x; y) = %sx + %sy$ (triệu đồng). \\\\
            Mối quan hệ giữa $x$ và $y$ được biểu diễn bởi hệ bất phương trình: $\\begin{cases} 2x + y \\ge %s \\\\ 2x + 5y \\ge %s \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$ \\\\
            Miền nghiệm của hệ bất phương trình là miền không bị gạch chứa các điểm $A(0; %s)$, $B(%s; %s)$, $C(%s; 0)$. \\\\
            Tính giá trị của $T(x; y)$ tại các đỉnh: \\\\
            - Tại $A(0; %s): T(0; %s) = %s \\cdot 0 + %s \\cdot %s = %s$ (triệu đồng). \\\\
            - Tại $B(%s; %s): T(%s; %s) = %s \\cdot %s + %s \\cdot %s = %s$ (triệu đồng). \\\\
            - Tại $C(%s; 0): T(%s; 0) = %s \\cdot %s + %s \\cdot 0 = %s$ (triệu đồng). \\\\
            So sánh các giá trị trên, ta thấy $T(x; y)$ đạt giá trị nhỏ nhất tại $B(%s; %s)$ với $T(%s; %s) = %s$ triệu đồng. %s \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (4,4);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (4,4);
            \\fill[white] (0, %s) -- (%s, %s) -- (%s, 0) -- (4,0) -- (4,4) -- (0,4) -- cycle;
            \\draw[black] (-2, %s) -- (4, %s);
            \\draw[black] (-2, %s) -- (4, %s);
            \\draw[black] (0, -2) -- (0, 4);
            \\coordinate (A) at (0,%s);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (%s,0);
            \\node at (A) [left] {$A$};
            \\node at (B) [right] {$B$};
            \\node at (C) [below] {$C$};
            \\fill (A) circle (1.5pt);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\draw[->] (-2, 0) -- (4, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 4) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (c_A, c_B, k1, k2, k1, x0, y0, xC_str,
                                k1, k1, c_A, c_B, k1, val_A,
                                x0, y0, x0, y0, c_A, x0, c_B, y0, val_B,
                                xC_str, xC_str, c_A, xC_str, c_B, val_C_str,
                                x0, y0, x0, y0, val_B, eval_vdc,
                                round(yA_p, 2), round(xB_p, 2), round(yB_p, 2), round(xC_p, 2),
                                round(l1_y_m2, 2), round(l1_y_4, 2),
                                round(l2_y_m2, 2), round(l2_y_4, 2),
                                round(yA_p, 2),
                                round(xB_p, 2), round(yB_p, 2),
                                round(xC_p, 2)))

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

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
            str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

