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


def bt_dang23_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên các tham số bài toán
            while True:
                # Chọn tọa độ giao điểm tối ưu (x0, y0) là điểm tối thiểu
                x0 = random.choice([4, 5, 6])
                y0 = random.choice([2, 3])

                # Giá thuê xe (triệu đồng)
                c_I = random.choice([4, 5])
                c_II = random.choice([3, 4])
                if c_I <= c_II:
                    continue

                # Thông số người và hàng
                nguoi_I = 20
                nguoi_II = 10
                hang_I = 0.5
                hang_II = 2.0

                # Tổng số người và hàng cần chở
                N = nguoi_I * x0 + nguoi_II * y0
                H_val = hang_I * x0 + hang_II * y0

                # Chọn tổng số hàng sao cho số thập phân đẹp (ví dụ ,5 hoặc nguyên)
                if H_val * 2 != int(H_val * 2):
                    continue

                H_str = "%g" % H_val
                H_str = H_str.replace('.', ',')

                # Số xe tối đa
                max_I = x0 + random.choice([3, 4])
                max_II = y0 + random.choice([5, 6])

                # Rút gọn hệ bất phương trình
                # 20x + 10y >= N <=> 2x + y >= k1
                k1 = 2 * x0 + y0

                # 0.5x + 2y >= H_val <=> x + 4y >= k2
                k2 = x0 + 4 * y0

                # Chi phí thấp nhất
                min_cost = c_I * x0 + c_II * y0
                fake_cost = min_cost + random.choice([2, 3])

                fake_x0 = x0 - 1
                fake_y0 = y0 + 1

                break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty cần thuê xe để chở %s người và %s tấn hàng. Nơi thuê xe có hai loại xe loại I và loại II, trong đó xe loại I có %s chiếc và loại xe II có %s chiếc. Một chiếc xe loại I cho thuê với giá %s triệu đồng, một chiếc xe loại II cho thuê với giá %s triệu đồng. Biết rằng mỗi chiếc xe loại I có thể chở tối đa 20 người và 0,5 tấn hàng; mỗi chiếc xe loại II có thể chở tối đa 10 người và 2 tấn hàng. Gọi $x$ và $y$ lần lượt là số xe loại I và loại II với $x, y \\in \\mathbb{N}$.''' % (N, H_str, max_I, max_II, c_I, c_II))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Hệ bất phương trình bậc nhất hai ẩn thỏa mãn điều kiện đề bài là $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 2x + y \\ge %s \\\\ x + 4y \\ge %s \\end{cases}$' % (max_I, max_II, k1, k2)
            nb_da_1_s = 'Hệ bất phương trình bậc nhất hai ẩn thỏa mãn điều kiện đề bài là $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 2x + y \\le %s \\\\ x + 4y \\le %s \\end{cases}$' % (max_I, max_II, k1, k2)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True Số tiền cần bỏ ra để thuê xe là $f(x; y) = %sx + %sy$' % (c_I, c_II)
            th_da_1_s = 'Số tiền cần bỏ ra để thuê xe là $f(x; y) = %sx + %sy$' % (c_II, c_I)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Số tiền thuê xe phải trả ít nhất là %s triệu đồng' % min_cost
            vd_da_1_s = 'Số tiền thuê xe phải trả ít nhất là %s triệu đồng' % fake_cost
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Để chi phí thuê xe là ít nhất thì cần phải thuê %s xe loại I và %s xe loại II' % (x0, y0)
            vdc_da_1_s = 'Để chi phí thuê xe là ít nhất thì cần phải thuê %s xe loại I và %s xe loại II' % (fake_x0, fake_y0)
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
                loigiai_nb_1 = ('Do số lượng xe loại I và loại II lần lượt là %s và %s nên ta có $0 \\le x \\le %s$ và $0 \\le y \\le %s$. \\\\'
                                'Số người cần chở là %s nên $20x + 10y \\ge %s \\iff 2x + y \\ge %s$. \\\\'
                                'Số tấn hàng cần chở là %s nên $0,5x + 2y \\ge %s \\iff x + 4y \\ge %s$. \\\\'
                                'Vậy ta có hệ bất phương trình $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 2x + y \\ge %s \\\\ x + 4y \\ge %s \\end{cases}$. Phát biểu trên là đúng.' % (max_I, max_II, max_I, max_II, N, N, k1, H_str, H_str, k2, max_I, max_II, k1, k2))
            else:
                loigiai_nb_1 = ('Do số lượng xe loại I và loại II lần lượt là %s và %s nên ta có $0 \\le x \\le %s$ và $0 \\le y \\le %s$. \\\\'
                                'Số người cần chở là %s nên $20x + 10y \\ge %s \\iff 2x + y \\ge %s$. \\\\'
                                'Số tấn hàng cần chở là %s nên $0,5x + 2y \\ge %s \\iff x + 4y \\ge %s$. \\\\'
                                'Vậy ta có hệ bất phương trình $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 2x + y \\ge %s \\\\ x + 4y \\ge %s \\end{cases}$. Phát biểu trên là sai.' % (max_I, max_II, max_I, max_II, N, N, k1, H_str, H_str, k2, max_I, max_II, k1, k2))

            # Lời giải Thông hiểu
            if '\\True' in th_da_1:
                loigiai_th_1 = ('Chi phí thuê $x$ xe loại I là $%sx$ (triệu đồng), chi phí thuê $y$ xe loại II là $%sy$ (triệu đồng). \\\\'
                                'Vậy số tiền cần bỏ ra để thuê xe là $f(x; y) = %sx + %sy$. Phát biểu trên là đúng.' % (c_I, c_II, c_I, c_II))
            else:
                loigiai_th_1 = ('Chi phí thuê $x$ xe loại I là $%sx$ (triệu đồng), chi phí thuê $y$ xe loại II là $%sy$ (triệu đồng). \\\\'
                                'Vậy số tiền cần bỏ ra để thuê xe là $f(x; y) = %sx + %sy$. Phát biểu trên là sai.' % (c_I, c_II, c_I, c_II))

            # Tính tọa độ các đỉnh của miền nghiệm
            # Các đường thẳng: x=0, x=max_I, y=0, y=max_II, d1: 2x+y=k1, d2: x+4y=k2
            # Các đỉnh (A, B, C, D)
            # B(x0, y0) là giao của 2x+y=k1 và x+4y=k2
            xB = x0
            yB = y0

            # Giao của d2 (x+4y=k2) và x=max_I => yC = (k2 - max_I)/4
            yC = (k2 - max_I) / 4.0
            xC = max_I

            # Giao của x=max_I và y=max_II => D(max_I, max_II)
            xD = max_I
            yD = max_II

            # Giao của y=max_II và d1 (2x+y=k1) => xE = (k1 - max_II)/2
            xE = (k1 - max_II) / 2.0
            yE = max_II

            # Điểm A là giao của d1(2x+y=k1) và x=0 => y = k1. 
            # Nhưng ở đây miền bị chặn bởi y<=max_II. Nên điểm đó là (xE, max_II) và một điểm (0, max_II)?
            # Xét d1 tại y=max_II => 2x = k1 - max_II => x = xE.
            # Tùy thuộc vào k1 và max_II, xE có thể âm hay dương. Ta giả sử xE dương.

            max_coord = max(max_I, max_II)
            S = max_coord / 4.0

            # Tính toán các đỉnh cụ thể để giải thích
            # A(0; k1) nếu k1 <= max_II, nhưng k1 thường > max_II.
            # Để đơn giản trong bài toán này, miền nghiệm là một đa giác. 
            # Các đỉnh là: giao của d1 với trục y (nếu y<=max_II), hoặc d1 với y=max_II.
            # Ta cứ lấy các đỉnh cơ bản: Giao 2 đường d1, d2 là (x0, y0).
            # Giao d2 với trục x là (k2, 0)
            # Nhưng x <= max_I. Nên điểm đó là (max_I, (k2-max_I)/4) nếu k2 > max_I.
            # Thường x0 < max_I, k2 = x0 + 4*y0 > max_I nếu y0 lớn.
            val_B = c_I * xB + c_II * yB
            val_C = c_I * xC + c_II * yC
            val_D = c_I * xD + c_II * yD
            val_E = c_I * xE + c_II * yE

            # Lời giải Vận dụng
            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('Bài toán đưa về tìm giá trị nhỏ nhất của hàm mục tiêu $f(x; y) = %sx + %sy$ trên miền nghiệm của hệ bất phương trình $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 2x + y \\ge %s \\\\ x + 4y \\ge %s \\end{cases}$. \\\\'
                                'Biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ, ta thấy giá trị nhỏ nhất đạt tại đỉnh có tọa độ $(%s; %s)$. \\\\'
                                'Khi đó $f_{min} = f(%s; %s) = %s \\cdot %s + %s \\cdot %s = %s$ (triệu đồng). Phát biểu trên là đúng.' % (c_I, c_II, max_I, max_II, k1, k2, x0, y0, x0, y0, c_I, x0, c_II, y0, min_cost))
            else:
                loigiai_vd_1 = ('Bài toán đưa về tìm giá trị nhỏ nhất của hàm mục tiêu $f(x; y) = %sx + %sy$ trên miền nghiệm của hệ bất phương trình $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 2x + y \\ge %s \\\\ x + 4y \\ge %s \\end{cases}$. \\\\'
                                'Biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ, ta thấy giá trị nhỏ nhất đạt tại đỉnh có tọa độ $(%s; %s)$. \\\\'
                                'Khi đó $f_{min} = f(%s; %s) = %s \\cdot %s + %s \\cdot %s = %s$ (triệu đồng). Phát biểu trên là sai.' % (c_I, c_II, max_I, max_II, k1, k2, x0, y0, x0, y0, c_I, x0, c_II, y0, min_cost))

            # Lời giải Vận dụng cao
            if '\\True' in vdc_da_1:
                loigiai_vdc_1 = ('Từ cách giải câu trên, chi phí thuê xe thấp nhất khi $(x; y) = (%s; %s)$. \\\\'
                                 'Nghĩa là công ty cần thuê %s xe loại I và %s xe loại II. Phát biểu trên là đúng.' % (x0, y0, x0, y0))
            else:
                loigiai_vdc_1 = ('Từ cách giải câu trên, chi phí thuê xe thấp nhất khi $(x; y) = (%s; %s)$. \\\\'
                                 'Nghĩa là công ty cần thuê %s xe loại I và %s xe loại II. Phát biểu trên là sai.' % (x0, y0, x0, y0))

            # Vẽ hình
            xB_p, yB_p = xB / S, yB / S
            xC_p, yC_p = xC / S, yC / S
            xD_p, yD_p = xD / S, yD / S
            xE_p, yE_p = xE / S, yE / S

            l1_y_m1 = (k1 - 2*(-1*S)) / S
            l1_y_7 = (k1 - 2*(7*S)) / S

            l2_y_m1 = (k2 - (-1*S)) / (4*S)
            l2_y_7 = (k2 - (7*S)) / (4*S)

            max_x_p = max_I / S
            max_y_p = max_II / S

            loigiai_vdc_1 += (''' \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-1,-1) rectangle (7,7);
            \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle (7,7);
            \\fill[white] (%s, %s) -- (%s, %s) -- (%s, %s) -- (%s, %s) -- cycle;
            \\draw[black] (-1, %s) -- (7, %s);
            \\draw[black] (-1, %s) -- (7, %s);
            \\draw[black] (%s, -1) -- (%s, 7);
            \\draw[black] (-1, %s) -- (7, %s);
            \\draw[black] (0, -1) -- (0, 7);
            \\draw[black] (-1, 0) -- (7, 0);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (%s,%s);
            \\coordinate (D) at (%s,%s);
            \\coordinate (E) at (%s,%s);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\fill (D) circle (1.5pt);
            \\fill (E) circle (1.5pt);
            \\draw[->] (-1, 0) -- (7, 0) node[below] {$x$};
            \\draw[->] (0, -1) -- (0, 7) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (round(xE_p,2), round(yE_p,2), round(xB_p,2), round(yB_p,2), round(xC_p,2), round(yC_p,2), round(xD_p,2), round(yD_p,2),
                                round(l1_y_m1, 2), round(l1_y_7, 2),
                                round(l2_y_m1, 2), round(l2_y_7, 2),
                                round(max_x_p, 2), round(max_x_p, 2),
                                round(max_y_p, 2), round(max_y_p, 2),
                                round(xB_p, 2), round(yB_p, 2),
                                round(xC_p, 2), round(yC_p, 2),
                                round(xD_p, 2), round(yD_p, 2),
                                round(xE_p, 2), round(yE_p, 2)))

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

