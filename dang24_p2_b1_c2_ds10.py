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


def bt_dang24_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random các thông số cho bất phương trình ax - by <= c (với a, b, c > 0)
            a = randint(1, 3)
            b = randint(2, 5)
            c = a * b * randint(1, 2)  # Để các giao điểm với trục tọa độ là số nguyên

            # Bất phương trình: ax - by <= c
            ineq_lhs = a*x - b*y
            c_val = c
            ineq_latex = '%s \\le %s' % (latex(ineq_lhs), latex(c_val))

            # Giao điểm với các trục
            x0 = c // a  # Giao với Ox (y=0) -> (x0, 0)
            y0 = -c // b # Giao với Oy (x=0) -> (0, y0)

            # Random một điểm M thuộc miền nghiệm cho câu a
            mx = randint(-5, 5)
            my = randint(-5, 5)
            val_M = a*mx - b*my
            is_M_true = val_M <= c
            if is_M_true:
                m_true_str = '\\True'
                m_false_str = ''
            else:
                m_true_str = ''
                m_false_str = '\\True'

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Cho bất phương trình bậc nhất hai ẩn: $%s \\ (1)$.''' 
                %(ineq_latex)
            )

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '%s Điểm $M(%s; %s)$ thuộc miền nghiệm của bất phương trình $(1)$' %(m_true_str, mx, my)
            nb_da_1_s = '%s Điểm $M(%s; %s)$ thuộc miền nghiệm của bất phương trình $(1)$' %(m_false_str, mx, my)
            list_nb_da_1 = [nb_da_1_d]
            if is_M_true:
                nb_da_1 = '\\True Điểm $M(%s; %s)$ thuộc miền nghiệm của bất phương trình $(1)$' %(mx, my)
            else:
                nb_da_1 = 'Điểm $M(%s; %s)$ thuộc miền nghiệm của bất phương trình $(1)$' %(mx, my)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            if is_M_true:
                loigiai_nb_1 = ('''Thay $x=%s, y=%s$ vào bất phương trình $(1)$ ta được: $%s \\cdot (%s) - %s \\cdot (%s) \\le %s \\Leftrightarrow %s \\le %s$ (đúng). \\\\ 
            Vậy điểm $M(%s; %s)$ thuộc miền nghiệm của bất phương trình $(1)$.'''
                    %(mx, my, a, mx, b, my, c, val_M, c, mx, my))
            else:
                loigiai_nb_1 = ('''Thay $x=%s, y=%s$ vào bất phương trình $(1)$ ta được: $%s \\cdot (%s) - %s \\cdot (%s) \\le %s \\Leftrightarrow %s \\le %s$ (sai). \\\\ 
            Vậy điểm $M(%s; %s)$ không thuộc miền nghiệm của bất phương trình $(1)$.'''
                    %(mx, my, a, mx, b, my, c, val_M, c, mx, my))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1 = '\\True Điểm $O(0; 0)$ thuộc miền nghiệm của bất phương trình $(1)$'
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thay $x=0, y=0$ vào bất phương trình $(1)$ ta được: $%s \\cdot 0 - %s \\cdot 0 \\le %s \\Leftrightarrow 0 \\le %s$ (đúng). \\\\ 
            Vậy điểm $O(0; 0)$ thuộc miền nghiệm của bất phương trình $(1)$.'''
                %(a, b, c, c)
            )

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Tính toán các tọa độ cho TikZ
            x_left = -2
            x_right = x0 + 2
            y_left = (a * x_left - c) / b
            y_right = (a * x_right - c) / b
            ymin_draw = math.floor(min(y_left, y0 - 1)) - 0.5
            ymax_draw = math.ceil(max(y_right, 3)) + 0.5

            # Hình đúng: Do 0 <= c (đúng), miền chứa O(0,0) là miền nghiệm (không bị gạch). Phần bị gạch là phía dưới đường thẳng.
            tikz_true = ('''\\\\ 
            \\begin{tikzpicture}[scale=0.6, >=stealth]
            \\draw[->] (%s,0) -- (%s,0) node[below] {$x$};
            \\draw[->] (0,%s) -- (0,%s) node[right] {$y$};
            \\node at (0.3,0.3) {$O$};
            \\draw[thick] (%s,%s) -- (%s,%s);
            \\fill[pattern=north east lines] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- cycle;
            \\node[above] at (%s,0) {$%s$};
            \\node[left] at (0,%s) {$%s$};
            \\end{tikzpicture}''' 
                % (x_left, x_right+1, ymin_draw, ymax_draw, 
                   x_left, y_left, x_right, y_right,
                   x_left, y_left, x_right, y_right, x_right, ymin_draw, x_left, ymin_draw,
                   x0, x0, y0, y0)
            )

            # Hình sai: Gạch nhầm phần chứa gốc tọa độ (phía trên đường thẳng)
            tikz_false = ('''\\\\ 
            \\begin{tikzpicture}[scale=0.6, >=stealth]
            \\draw[->] (%s,0) -- (%s,0) node[below] {$x$};
            \\draw[->] (0,%s) -- (0,%s) node[right] {$y$};
            \\node at (0.3,0.3) {$O$};
            \\draw[thick] (%s,%s) -- (%s,%s);
            \\fill[pattern=north east lines] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- cycle;
            \\node[above] at (%s,0) {$%s$};
            \\node[left] at (0,%s) {$%s$};
            \\end{tikzpicture}''' 
                % (x_left, x_right+1, ymin_draw, ymax_draw, 
                   x_left, y_left, x_right, y_right,
                   x_left, y_left, x_right, y_right, x_right, ymax_draw, x_left, ymax_draw,
                   x0, x0, y0, y0)
            )

            # Các đáp án
            vd_da_1_d = '\\True Miền nghiệm của bất phương trình là miền không bị gạch được biểu diễn như hình: %s' % tikz_true
            vd_da_1_s = 'Miền nghiệm của bất phương trình là miền không bị gạch được biểu diễn như hình: %s' % tikz_false
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('''Vẽ đường thẳng $d: %s = %s$. \\\\ 
            Cho $x = 0 \\Rightarrow y = %s$, ta được điểm $(0; %s)$. \\\\ 
            Cho $y = 0 \\Rightarrow x = %s$, ta được điểm $(%s; 0)$. \\\\ 
            Đường thẳng $d$ đi qua hai điểm $(0; %s)$ và $(%s; 0)$. \\\\ 
            Vì $0 \\le %s$ là mệnh đề đúng nên miền nghiệm của bất phương trình chứa điểm $O(0; 0)$. \\\\ 
            Hình vẽ đã cho biểu diễn chính xác miền nghiệm (miền không bị gạch, kể cả bờ $d$).'''
                    %(latex(ineq_lhs), c, y0, y0, x0, x0, y0, x0, c))
            else:
                loigiai_vd_1 = ('''Vẽ đường thẳng $d: %s = %s$. \\\\ 
            Cho $x = 0 \\Rightarrow y = %s$, ta được điểm $(0; %s)$. \\\\ 
            Cho $y = 0 \\Rightarrow x = %s$, ta được điểm $(%s; 0)$. \\\\ 
            Đường thẳng $d$ đi qua hai điểm $(0; %s)$ và $(%s; 0)$. \\\\ 
            Vì $0 \\le %s$ là mệnh đề đúng nên miền nghiệm của bất phương trình phải chứa điểm $O(0; 0)$. \\\\ 
            Tuy nhiên, hình vẽ đã gạch bỏ miền chứa gốc $O(0; 0)$ nên hình vẽ này là sai.'''
                    %(latex(ineq_lhs), c, y0, y0, x0, x0, y0, x0, c))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1 = 'Có $10$ điểm có tọa độ là các bộ số nguyên dương thuộc miền nghiệm của bất phương trình trên'
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét hệ $\\begin{cases} %s \\le %s \\\\ x \\ge 1 \\\\ y \\ge 1 \\end{cases}$. \\\\ 
            Từ bất phương trình ta có $x \\le \\frac{%s + %sy}{%s}$. \\\\ 
            Với mỗi $y \\in \\mathbb{N}^*$, ta luôn tìm được vô số giá trị $x \\in \\mathbb{N}^*$ thỏa mãn bất phương trình. \\\\ 
            Vậy có vô số điểm có tọa độ là số nguyên dương thuộc miền nghiệm, nên phát biểu là sai.'''
                %(latex(ineq_lhs), c, c, b, a)
            )

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo số đáp án đúng từ 1 đến 3
            while True:
                nb_da_1 = list_nb_1[0]
                th_da_1 = list_th_1[0]
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = list_vdc_1[0]

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Cập nhật lại list Vận dụng theo đáp án đã chọn
            list_vd_1 = [vd_da_1]
            if '\\True' in vd_da_1:
                list_vd_2 = [('''Vẽ đường thẳng $d: %s = %s$. \\\\ 
            Cho $x = 0 \\Rightarrow y = %s$, ta được điểm $(0; %s)$. \\\\ 
            Cho $y = 0 \\Rightarrow x = %s$, ta được điểm $(%s; 0)$. \\\\ 
            Đường thẳng $d$ đi qua hai điểm $(0; %s)$ và $(%s; 0)$. \\\\ 
            Vì $0 \\le %s$ là mệnh đề đúng nên miền nghiệm của bất phương trình chứa điểm $O(0; 0)$. \\\\ 
            Hình vẽ đã cho biểu diễn chính xác miền nghiệm (miền không bị gạch, kể cả bờ $d$).'''
                    %(latex(ineq_lhs), c, y0, y0, x0, x0, y0, x0, c))]
            else:
                list_vd_2 = [('''Vẽ đường thẳng $d: %s = %s$. \\\\ 
            Cho $x = 0 \\Rightarrow y = %s$, ta được điểm $(0; %s)$. \\\\ 
            Cho $y = 0 \\Rightarrow x = %s$, ta được điểm $(%s; 0)$. \\\\ 
            Đường thẳng $d$ đi qua hai điểm $(0; %s)$ và $(%s; 0)$. \\\\ 
            Vì $0 \\le %s$ là mệnh đề đúng nên miền nghiệm của bất phương trình phải chứa điểm $O(0; 0)$. \\\\ 
            Tuy nhiên, hình vẽ đã gạch bỏ miền chứa gốc $O(0; 0)$ nên hình vẽ này là sai.'''
                    %(latex(ineq_lhs), c, y0, y0, x0, x0, y0, x0, c))]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
            str(noidungcauhoi) +
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

