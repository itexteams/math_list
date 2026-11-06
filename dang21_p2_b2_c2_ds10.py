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


def bt_dang21_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên các tham số bài toán
            while True:
                k = random.choice([2, 3, 4])
                min_y = random.choice([20, 30, 40, 50])

                # max_total = x + y, with x >= k*y => max_total >= (k+1)*min_y
                # Let's pick a max_total larger than (k+1)*min_y
                min_total = (k + 1) * min_y
                max_total = min_total + random.choice([40, 60, 80, 100])

                if max_total % (k + 1) != 0:
                    continue

                break

            # Tính toán các đỉnh của miền nghiệm
            # Hệ BPT:
            # 1) x + y <= max_total
            # 2) y >= min_y
            # 3) x >= k*y  <=> x - k*y >= 0

            # Đỉnh A: giao của y = min_y và x = k*y => x = k*min_y, y = min_y
            xA = k * min_y
            yA = min_y

            # Đỉnh B: giao của x + y = max_total và x = k*y => k*y + y = max_total => y = max_total / (k+1)
            yB = int(max_total / (k + 1))
            xB = k * yB

            # Đỉnh C: giao của x + y = max_total và y = min_y => x = max_total - min_y
            yC = min_y
            xC = max_total - min_y

            # Random một điểm (x_test, y_test)
            x_test = random.choice([xA + 10, xB + 10])
            y_test = min_y
            test_point_valid = (x_test + y_test <= max_total) and (y_test >= min_y) and (x_test >= k * y_test)

            min_sum = xA + yA
            fake_min_sum = min_sum + 20

            # Nội dung câu hỏi
            noidungcauhoi = ('''Chị Hằng có kế hoạch đầu tư không quá %s triệu đồng vào hai dự án: dự án $I$ là cho thuê xe đạp trong ngày quanh khu du lịch sinh thái và dự án $II$ là chụp ảnh kỷ yếu cho học sinh. Để đạt được lợi nhuận thì khoản dự án $II$ phải đầu tư ít nhất %s triệu đồng và số tiền đầu tư cho khoản dự án $I$ phải ít nhất gấp %s lần số tiền cho dự án $II$.''' % (max_total, min_y, k))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Gọi $x, y$ lần lượt là số tiền chị Hằng đầu tư vào dự án $I$ và $II$. Khi đó ta có hệ bất phương trình: $\\begin{cases} x + y \\le %s \\\\ y \\ge %s \\\\ x \\ge %s y \\end{cases}$' % (max_total, min_y, k)
            nb_da_1_s = 'Gọi $x, y$ lần lượt là số tiền chị Hằng đầu tư vào dự án $I$ và $II$. Khi đó ta có hệ bất phương trình: $\\begin{cases} x + y \\le %s \\\\ y \\ge %s \\\\ y \\ge %s x \\end{cases}$' % (max_total, min_y, k)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True Đầu tư %s triệu đồng cho dự án $I$ và %s triệu đồng cho dự án $II$ thỏa tất cả điều kiện chị Hằng cần đầu tư vào hai dự án' % (x_test, y_test) if test_point_valid else '\\True Đầu tư %s triệu đồng cho dự án $I$ và %s triệu đồng cho dự án $II$ không thỏa tất cả điều kiện chị Hằng cần đầu tư vào hai dự án' % (x_test, y_test + 50)
            th_da_1_s = 'Đầu tư %s triệu đồng cho dự án $I$ và %s triệu đồng cho dự án $II$ không thỏa tất cả điều kiện chị Hằng cần đầu tư vào hai dự án' % (x_test, y_test) if test_point_valid else 'Đầu tư %s triệu đồng cho dự án $I$ và %s triệu đồng cho dự án $II$ thỏa tất cả điều kiện chị Hằng cần đầu tư vào hai dự án' % (x_test, y_test + 50)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình thỏa điều kiện chị Hằng đầu tư vào hai dự án là một tam giác'
            vd_da_1_s = 'Miền nghiệm của hệ bất phương trình thỏa điều kiện chị Hằng đầu tư vào hai dự án là một tứ giác'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng số tiền đầu tư vào hai dự án ít nhất bằng %s triệu đồng' % min_sum
            vdc_da_1_s = 'Tổng số tiền đầu tư vào hai dự án ít nhất bằng %s triệu đồng' % fake_min_sum
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
                loigiai_nb_1 = ('Đầu tư không quá %s triệu đồng vào hai dự án nên $x + y \\le %s$. \\\\ Dự án $II$ phải đầu tư ít nhất %s triệu đồng nên $y \\ge %s$. \\\\ Số tiền đầu tư cho khoản dự án $I$ phải ít nhất gấp %s lần số tiền cho dự án $II$ nên $x \\ge %sy$. \\\\ Vậy ta có hệ bất phương trình $\\begin{cases} x + y \\le %s \\\\ y \\ge %s \\\\ x \\ge %s y \\end{cases}$. Do đó phát biểu trên là đúng.' % (max_total, max_total, min_y, min_y, k, k, max_total, min_y, k))
            else:
                loigiai_nb_1 = ('Đầu tư không quá %s triệu đồng vào hai dự án nên $x + y \\le %s$. \\\\ Dự án $II$ phải đầu tư ít nhất %s triệu đồng nên $y \\ge %s$. \\\\ Số tiền đầu tư cho khoản dự án $I$ phải ít nhất gấp %s lần số tiền cho dự án $II$ nên $x \\ge %sy$. \\\\ Vậy ta có hệ bất phương trình $\\begin{cases} x + y \\le %s \\\\ y \\ge %s \\\\ x \\ge %s y \\end{cases}$. Do đó phát biểu trên là sai.' % (max_total, max_total, min_y, min_y, k, k, max_total, min_y, k))

            # Lời giải Thông hiểu
            x_t = x_test
            y_t = y_test if test_point_valid else y_test + 50
            is_valid_test = (x_t + y_t <= max_total) and (y_t >= min_y) and (x_t >= k * y_t)

            if '\\True' in th_da_1:
                if is_valid_test:
                    loigiai_th_1 = ('Thay $x = %s, y = %s$ vào hệ bất phương trình ta thấy thỏa mãn. Do đó phát biểu trên là đúng.' % (x_t, y_t))
                else:
                    loigiai_th_1 = ('Thay $x = %s, y = %s$ vào hệ bất phương trình ta thấy không thỏa mãn. Do đó phát biểu trên là đúng.' % (x_t, y_t))
            else:
                if is_valid_test:
                    loigiai_th_1 = ('Thay $x = %s, y = %s$ vào hệ bất phương trình ta thấy thỏa mãn. Do đó phát biểu trên là sai.' % (x_t, y_t))
                else:
                    loigiai_th_1 = ('Thay $x = %s, y = %s$ vào hệ bất phương trình ta thấy không thỏa mãn. Do đó phát biểu trên là sai.' % (x_t, y_t))

            # Lời giải Vận dụng
            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('Vẽ các đường thẳng $d_1: x + y = %s$, $d_2: y = %s$, $d_3: x - %sy = 0$. \\\\ Miền nghiệm của hệ bất phương trình là miền tam giác (kể cả biên) với các đỉnh $A(%s; %s)$, $B(%s; %s)$, $C(%s; %s)$. Do đó phát biểu trên là đúng.' % (max_total, min_y, k, xA, yA, xB, yB, xC, yC))
            else:
                loigiai_vd_1 = ('Vẽ các đường thẳng $d_1: x + y = %s$, $d_2: y = %s$, $d_3: x - %sy = 0$. \\\\ Miền nghiệm của hệ bất phương trình là miền tam giác (kể cả biên) với các đỉnh $A(%s; %s)$, $B(%s; %s)$, $C(%s; %s)$. Do đó phát biểu trên là sai.' % (max_total, min_y, k, xA, yA, xB, yB, xC, yC))

            # Vẽ hình
            max_coord = max(xC, yB)
            S = max_coord / 3.5

            xA_p = xA / S
            yA_p = yA / S
            xB_p = xB / S
            yB_p = yB / S
            xC_p = xC / S
            yC_p = yC / S

            # Lines for clip (-1, -1) to (5, 5)
            # L1: x + y = max_total => y = max_total/S - x
            l1_y_m1 = max_total/S - (-1)
            l1_y_5 = max_total/S - (5)

            # L2: y = min_y
            l2_y = min_y / S

            # L3: x = k*y => y = x/k
            l3_y_m1 = -1 / k
            l3_y_5 = 5 / k

            # Lời giải Vận dụng cao
            if '\\True' in vdc_da_1:
                eval_vdc = "Do đó phát biểu trên là đúng."
            else:
                eval_vdc = "Do đó phát biểu trên là sai."

            loigiai_vdc_1 = ('''Tổng số tiền đầu tư là $F(x; y) = x + y$. \\\\
            Tính giá trị của $F(x; y)$ tại các đỉnh của miền nghiệm tam giác $ABC$: \\\\
            - Tại $A(%s; %s): F(%s; %s) = %s + %s = %s$. \\\\
            - Tại $B(%s; %s): F(%s; %s) = %s + %s = %s$. \\\\
            - Tại $C(%s; %s): F(%s; %s) = %s + %s = %s$. \\\\
            So sánh các giá trị trên, ta thấy $F(x; y)$ đạt giá trị nhỏ nhất tại $A(%s; %s)$ với $F(%s; %s) = %s$. %s \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-1,-1) rectangle (5,5);
            \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle (5,5);
            \\fill[white] (%s, %s) -- (%s, %s) -- (%s, %s) -- cycle;
            \\draw[black] (-1, %s) -- (5, %s);
            \\draw[black] (-1, %s) -- (5, %s);
            \\draw[black] (-1, %s) -- (5, %s);
            \\draw[black] (0, -1) -- (0, 5);
            \\coordinate (A) at (%s,%s);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (%s,%s);
            \\node at (A) [below left] {$A$};
            \\node at (B) [above right] {$B$};
            \\node at (C) [below right] {$C$};
            \\fill (A) circle (1.5pt);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\draw[->] (-1, 0) -- (5, 0) node[below] {$x$};
            \\draw[->] (0, -1) -- (0, 5) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (xA, yA, xA, yA, xA, yA, xA + yA,
                                xB, yB, xB, yB, xB, yB, xB + yB,
                                xC, yC, xC, yC, xC, yC, xC + yC,
                                xA, yA, xA, yA, xA + yA, eval_vdc,
                                round(xA_p, 2), round(yA_p, 2), round(xB_p, 2), round(yB_p, 2), round(xC_p, 2), round(yC_p, 2),
                                round(l1_y_m1, 2), round(l1_y_5, 2),
                                round(l2_y, 2), round(l2_y, 2),
                                round(l3_y_m1, 2), round(l3_y_5, 2),
                                round(xA_p, 2), round(yA_p, 2),
                                round(xB_p, 2), round(yB_p, 2),
                                round(xC_p, 2), round(yC_p, 2)))

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

