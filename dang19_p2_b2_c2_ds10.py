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


def bt_dang19_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên các số trong bài toán
            while True:
                xB = random.choice([10, 15, 20, 25, 30])
                yB = random.choice([20, 30, 40, 50])

                t11 = random.choice([3, 4, 5])
                t12 = random.choice([2, 3, 4])
                t21 = random.choice([1, 2, 3])
                t22 = random.choice([4, 5, 6])

                if t11 * t22 - t12 * t21 <= 0:
                    continue

                T1 = t11 * xB + t12 * yB
                T2 = t21 * xB + t22 * yB

                if T1 % t11 != 0 or T2 % t22 != 0:
                    continue

                yA = T2 // t22
                xC = T1 // t11

                if xC <= xB or yA <= yB:
                    continue

                p_candidates = []
                for p1 in range(300, 1000, 100):
                    for p2 in range(300, 1000, 100):
                        if (t21 * p2 < p1 * t22) and (p1 * t12 < t11 * p2):
                            p_candidates.append((p1, p2))

                if not p_candidates:
                    continue

                p1, p2 = random.choice(p_candidates)

                total_profit_thousand = p1 * xB + p2 * yB
                if total_profit_thousand % 1000 == 0:
                    profit_str = "%s triệu đồng" % (total_profit_thousand // 1000)
                else:
                    profit_str = "%s nghìn đồng" % total_profit_thousand

                fake_profit_val = p1 * xC if (p1 * xC != total_profit_thousand) else p2 * yA
                if fake_profit_val % 1000 == 0:
                    fake_profit_str = "%s triệu đồng" % (fake_profit_val // 1000)
                else:
                    fake_profit_str = "%s nghìn đồng" % fake_profit_val

                break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một xưởng cơ khí có hai công nhân là Thành và Công. Xưởng sản xuất loại sản phẩm I và II. Mỗi sản phẩm I bán lãi %s nghìn đồng, mỗi sản phẩm II bán lãi %s nghìn đồng. Để sản xuất được một sản phẩm I thì Thành phải làm việc trong %s giờ, Công phải làm việc trong %s giờ. Để sản xuất được một sản phẩm II thì Thành phải làm việc trong %s giờ, Công phải làm việc trong %s giờ. Một người không thể làm đồng thời hai sản phẩm. Biết rằng trong một tháng Thành không thể làm việc quá %s giờ và Công không thể làm việc quá %s giờ. Gọi $x; y$ ($x; y \\in \\mathbb{N}$) lần lượt là số sản phẩm loại I và loại II được sản xuất ra.''' % (p1, p2, t11, t21, t12, t22, T1, T2))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Vì một tháng Thành không thể làm việc quá %s giờ nên ta có bất phương trình $%sx + %sy \\le %s$' % (T1, t11, t12, T1)
            nb_da_1_s = 'Vì một tháng Thành không thể làm việc quá %s giờ nên ta có bất phương trình $%sx + %sy \\le %s$' % (T1, t11, t21, T1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True Hệ bất phương trình bậc nhất hai ẩn thể hiện mối quan hệ giữa $x$ và $y$ là $\\begin{cases} %sx + %sy \\le %s \\\\ %sx + %sy \\le %s \\\\ x \\in \\mathbb{N} \\\\ y \\in \\mathbb{N} \\end{cases}$' % (t11, t12, T1, t21, t22, T2)
            th_da_1_s = 'Hệ bất phương trình bậc nhất hai ẩn thể hiện mối quan hệ giữa $x$ và $y$ là $\\begin{cases} %sx + %sy \\le %s \\\\ %sx + %sy \\le %s \\\\ x \\in \\mathbb{N} \\\\ y \\in \\mathbb{N} \\end{cases}$' % (t11, t21, T1, t12, t22, T2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Miền nghiệm của hệ là miền tứ giác $OABC$ với $A(0; %s)$, $B(%s; %s)$, $C(%s; 0)$, $O(0; 0)$' % (yA, xB, yB, xC)
            vd_da_1_s = 'Miền nghiệm của hệ là miền tứ giác $OABC$ với $A(0; %s)$, $B(%s; %s)$, $C(%s; 0)$, $O(0; 0)$' % (yA + 2, xB, yB, xC)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tiền lãi lớn nhất của xưởng trong một tháng là %s' % profit_str
            vdc_da_1_s = 'Tiền lãi lớn nhất của xưởng trong một tháng là %s' % fake_profit_str
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
                loigiai_nb_1 = ('''Số giờ làm việc của Thành để sản xuất $x$ sản phẩm loại I và $y$ sản phẩm loại II là $%sx + %sy$ (giờ). \\\\ Vì một tháng Thành không thể làm việc quá %s giờ nên ta có bất phương trình $%sx + %sy \\le %s$. Do đó phát biểu trên là đúng.''' % (t11, t12, T1, t11, t12, T1))
            else:
                loigiai_nb_1 = ('''Số giờ làm việc của Thành để sản xuất $x$ sản phẩm loại I và $y$ sản phẩm loại II là $%sx + %sy$ (giờ). \\\\ Vì một tháng Thành không thể làm việc quá %s giờ nên ta có bất phương trình $%sx + %sy \\le %s$. Do đó phát biểu trên là sai.''' % (t11, t12, T1, t11, t12, T1))

            # Lời giải Thông hiểu
            if '\\True' in th_da_1:
                loigiai_th_1 = ('''Số giờ làm việc của Thành là $%sx + %sy \\le %s$. \\\\ Số giờ làm việc của Công là $%sx + %sy \\le %s$. \\\\ Vì $x, y$ là số sản phẩm nên $x \\in \\mathbb{N}, y \\in \\mathbb{N}$. \\\\ Do đó hệ bất phương trình biểu diễn mối quan hệ giữa $x$ và $y$ là $\\begin{cases} %sx + %sy \\le %s \\\\ %sx + %sy \\le %s \\\\ x \\in \\mathbb{N} \\\\ y \\in \\mathbb{N} \\end{cases}$. Do đó phát biểu trên là đúng.''' % (t11, t12, T1, t21, t22, T2, t11, t12, T1, t21, t22, T2))
            else:
                loigiai_th_1 = ('''Số giờ làm việc của Thành là $%sx + %sy \\le %s$. \\\\ Số giờ làm việc của Công là $%sx + %sy \\le %s$. \\\\ Vì $x, y$ là số sản phẩm nên $x \\in \\mathbb{N}, y \\in \\mathbb{N}$. \\\\ Do đó hệ bất phương trình đúng phải là $\\begin{cases} %sx + %sy \\le %s \\\\ %sx + %sy \\le %s \\\\ x \\in \\mathbb{N} \\\\ y \\in \\mathbb{N} \\end{cases}$. Do đó phát biểu trên là sai.''' % (t11, t12, T1, t21, t22, T2, t11, t12, T1, t21, t22, T2))

            # Lời giải Vận dụng
            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('''Vẽ các đường thẳng $d_1: %sx + %sy = %s$, $d_2: %sx + %sy = %s$, trục $Ox$ và trục $Oy$. \\\\ Miền nghiệm của hệ là miền tứ giác $OABC$ (kể cả biên) với các đỉnh $O(0; 0)$, $A(0; %s)$, $B(%s; %s)$, $C(%s; 0)$. Do đó phát biểu trên là đúng.''' % (t11, t12, T1, t21, t22, T2, yA, xB, yB, xC))
            else:
                loigiai_vd_1 = ('''Vẽ các đường thẳng $d_1: %sx + %sy = %s$, $d_2: %sx + %sy = %s$, trục $Ox$ và trục $Oy$. \\\\ Miền nghiệm của hệ là miền tứ giác $OABC$ (kể cả biên) với các đỉnh $O(0; 0)$, $A(0; %s)$, $B(%s; %s)$, $C(%s; 0)$. Do đó phát biểu trên là sai.''' % (t11, t12, T1, t21, t22, T2, yA, xB, yB, xC))

            # Tính toán các tỷ lệ phục vụ việc vẽ hình trong clip (-2,-2) to (4,4)
            max_val = max(xC, yA)
            S = max_val / 3.0 # Tỷ lệ thu phóng hệ tọa độ về khoảng ~3 đơn vị độ dài
            xA_p = 0
            yA_p = yA / S
            xB_p = xB / S
            yB_p = yB / S
            xC_p = xC / S
            yC_p = 0

            # Tính y tại các điểm cắt giới hạn khung vẽ x=-2 và x=4 cho 2 đường
            l1_y_m2 = (T1/S - t11*(-2))/t12
            l1_y_4 = (T1/S - t11*(4))/t12
            l2_y_m2 = (T2/S - t21*(-2))/t22
            l2_y_4 = (T2/S - t21*(4))/t22

            # Lời giải Vận dụng cao
            val_A = p2 * yA
            val_B = total_profit_thousand
            val_C = p1 * xC

            if '\\True' in vdc_da_1:
                eval_vdc = "Do đó phát biểu trên là đúng."
            else:
                eval_vdc = "Do đó phát biểu trên là sai."

            loigiai_vdc_1 = ('''Tổng số tiền lãi nhận được trong một tháng là $F(x; y) = %sx + %sy$ (nghìn đồng). \\\\
            Tính giá trị của $F(x; y)$ tại các đỉnh của miền nghiệm tứ giác $OABC$: \\\\
            - Tại $O(0; 0): F(0; 0) = 0$ (nghìn đồng). \\\\
            - Tại $A(0; %s): F(0; %s) = %s \\cdot 0 + %s \\cdot %s = %s$ (nghìn đồng). \\\\
            - Tại $B(%s; %s): F(%s; %s) = %s \\cdot %s + %s \\cdot %s = %s$ (nghìn đồng). \\\\
            - Tại $C(%s; 0): F(%s; 0) = %s \\cdot %s + %s \\cdot 0 = %s$ (nghìn đồng). \\\\
            So sánh các giá trị trên, ta thấy $F(x; y)$ đạt giá trị lớn nhất tại $B(%s; %s)$ với $F(%s; %s) = %s$ (nghìn đồng), tức là %s. %s \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (4,4);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (4,4);
            \\fill[white] (0, 0) -- (%s, 0) -- (%s, %s) -- (0, %s) -- cycle;
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
            \\end{center}''' % (p1, p2,
                                yA, yA, p1, p2, yA, val_A,
                                xB, yB, xB, yB, p1, xB, p2, yB, val_B,
                                xC, xC, p1, xC, p2, val_C,
                                xB, yB, xB, yB, val_B, profit_str, eval_vdc,
                                round(xC_p, 2), round(xB_p, 2), round(yB_p, 2), round(yA_p, 2),
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

