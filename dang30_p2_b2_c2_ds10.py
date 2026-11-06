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


def bt_dang30_p2_b2_c2_ds10(self):
            # Khai báo biến
            def format_money(amount):
                return "{:,}".format(amount * 1000).replace(",", " ")

            # Khai báo biến
            k1 = random.randint(2, 5)
            k2 = random.randint(1, 3)
            PL = random.choice([400, 450, 500, 550, 600])
            PS = random.choice([300, 350, 400])

            tong_bo = 40 * k1
            bo_L = 5 * k1
            bo_S = 4 * k1

            tong_thuc_an = 30 * k2
            thuc_an_L = 5 * k2
            thuc_an_S = 2 * k2

            FA = 4 * PL + 5 * PS
            FB = 2 * PL + 10 * PS
            FC = 9 * PL + 10 * PS
            FD = 9 * PL
            FE = 8 * PL
            min_cost = min(FA, FB, FC, FD, FE)
            fake_min_cost = min_cost - 50

            min_cost_str = format_money(min_cost)
            fake_min_cost_str = format_money(fake_min_cost)

            # Nội dung câu hỏi
            noidungcauhoi = ('Một trang trại cần thuê xe để vận chuyển một lúc $%s$ con bò sữa và $%s$ tấn thức ăn cho bò. Nơi cho thuê chỉ có $9$ xe lớn và $10$ xe nhỏ. Một chiếc xe lớn chỉ có thể chở được $%s$ con bò và $%s$ tấn thức ăn. Một chiếc xe nhỏ chỉ có thể chở được $%s$ con bò và $%s$ tấn thức ăn. Giá thuê của một chiếc xe lớn là $%s$ nghìn đồng và một chiếc xe nhỏ là $%s$ nghìn đồng. Gọi $x; y$ lần lượt là số xe lớn, xe nhỏ chủ trang trại cần thuê.'
                             % (tong_bo, tong_thuc_an, bo_L, thuc_an_L, bo_S, thuc_an_S, PL, PS))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chi phí chủ trang trại thuê xe phải trả là $F(x;y)=%s x+%s y$.' % (PL, PS)
            nb_da_1_s = 'Chi phí chủ trang trại thuê xe phải trả là $F(x;y)=%s x+%s y$.' % (PS, PL)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Chi phí chủ trang trại thuê xe phải trả là tổng chi phí thuê $x$ xe lớn và $y$ xe nhỏ, do đó $F(x;y)=%s x+%s y$.'
                            % (PL, PS))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hệ bất phương trình biểu thị giả thiết bài toán là $\\begin{cases} 0 \\le x \\le 9 \\\\ 0 \\le y \\le 10 \\\\ %s x+%s y \\ge %s \\\\ %s x+%s y \\ge %s \\end{cases}$.' % (bo_L, bo_S, tong_bo, thuc_an_L, thuc_an_S, tong_thuc_an)
            th_da_1_s = 'Hệ bất phương trình biểu thị giả thiết bài toán là $\\begin{cases} 0 \\le x \\le 9 \\\\ 0 \\le y \\le 10 \\\\ %s x+%s y \\le %s \\\\ %s x+%s y \\le %s \\end{cases}$.' % (bo_L, bo_S, tong_bo, thuc_an_L, thuc_an_S, tong_thuc_an)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Số xe lớn tối đa là $9$ nên $0 \\le x \\le 9$. \\\\ Số xe nhỏ tối đa là $10$ nên $0 \\le y \\le 10$. \\\\ Tổng số bò chở được là $%s x+%s y$, phải lớn hơn hoặc bằng $%s$ nên $%s x+%s y \\ge %s$. \\\\ Tổng số thức ăn chở được là $%s x+%s y$, phải lớn hơn hoặc bằng $%s$ nên $%s x+%s y \\ge %s$. \\\\ Vậy ta có hệ: $\\begin{cases} 0 \\le x \\le 9 \\\\ 0 \\le y \\le 10 \\\\ %s x+%s y \\ge %s \\\\ %s x+%s y \\ge %s \\end{cases}$.'
                            % (bo_L, bo_S, tong_bo, bo_L, bo_S, tong_bo, thuc_an_L, thuc_an_S, tong_thuc_an, thuc_an_L, thuc_an_S, tong_thuc_an, bo_L, bo_S, tong_bo, thuc_an_L, thuc_an_S, tong_thuc_an))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Miền nghiệm của bất phương trình trên là miền ngũ giác $ABCDE$ với $A(4;5), B(2;10), C(9;10), D(9;0), E(8;0)$.'
            vd_da_1_s = 'Miền nghiệm của bất phương trình trên là miền tứ giác $ABCD$ với $A(4;5), B(2;10), C(9;10), D(8;0)$.'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Vẽ các đường thẳng $d_1\\colon %s x+%s y=%s$ (tương đương $5x+4y=40$) và $d_2\\colon %s x+%s y=%s$ (tương đương $5x+2y=30$), $x=9, y=10$. \\\\ Xác định miền nghiệm của hệ bất phương trình ta được miền ngũ giác không bị gạch (kể cả biên) trong hình vẽ dưới đây: \\\\ \\begin{center} \\begin{tikzpicture}[>=stealth, scale=0.4, line width=1pt] \\draw[->] (-2, 0) -- (12, 0) node[below] {$x$}; \\draw[->] (0, -2) -- (0, 13) node[left] {$y$}; \\node at (0,0) [below left] {$O$}; \\clip (-2,-2) rectangle (12,13); \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (12,13); \\fill[white] (2,10) -- (9,10) -- (9,0) -- (8,0) -- (4,5) -- cycle; \\draw[black] (9,-2) -- (9,13); \\draw[black] (-2,10) -- (12,10); \\draw[black] (-4,15) -- (12,-5); \\draw[black] (-2,20) -- (8,-5); \\coordinate (B) at (2,10); \\coordinate (C) at (9,10); \\coordinate (D) at (9,0); \\coordinate (E) at (8,0); \\coordinate (A) at (4,5); \\fill (A) circle (3.5pt) node[below left] {$A$}; \\fill (B) circle (3.5pt) node[above left] {$B$}; \\fill (C) circle (3.5pt) node[above right] {$C$}; \\fill (D) circle (3.5pt) node[below right] {$D$}; \\fill (E) circle (3.5pt) node[below left] {$E$}; \\end{tikzpicture} \\end{center} Các đỉnh của ngũ giác là $A(4;5), B(2;10), C(9;10), D(9;0), E(8;0)$.'
                            % (bo_L, bo_S, tong_bo, thuc_an_L, thuc_an_S, tong_thuc_an))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Chi phí thuê xe là nhỏ nhất là $%s$ đồng.' % (min_cost_str)
            vdc_da_1_s = 'Chi phí thuê xe là nhỏ nhất là $%s$ đồng.' % (fake_min_cost_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta tính giá trị của $F(x;y)=%s x+%s y$ tại các đỉnh của miền nghiệm: \\\\ $F(4;5) = %s \\cdot 4 + %s \\cdot 5 = %s$ \\\\ $F(2;10) = %s \\cdot 2 + %s \\cdot 10 = %s$ \\\\ $F(9;10) = %s \\cdot 9 + %s \\cdot 10 = %s$ \\\\ $F(9;0) = %s \\cdot 9 + %s \\cdot 0 = %s$ \\\\ $F(8;0) = %s \\cdot 8 + %s \\cdot 0 = %s$ \\\\ Vậy chi phí thuê xe nhỏ nhất là $%s$ đồng (tương ứng thuê $4$ xe lớn và $5$ xe nhỏ).'
                             % (PL, PS, PL, PS, FA, PL, PS, FB, PL, PS, FC, PL, PS, FD, PL, PS, FE, min_cost_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

