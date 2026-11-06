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


def bt_dang9_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Khởi tạo các giá trị ngẫu nhiên
            # Chọn 2 nghiệm nguyên để bài toán đẹp (x1 < x2)
            x1 = random.randint(-5, 0)
            x2 = random.randint(1, 6)
            # Hàm số mặc định hệ số a = -1 như trong ảnh: f(x) = -(x - x1)(x - x2)
            f_x = sp.expand(-(x - x1)*(x - x2))
            a_coeff = -1
            b_coeff = x1 + x2
            c_coeff = -x1 * x2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam thức bậc hai $f(x) = %s$.''' 
                             % (latex(f_x)))

            ########################################################################
            # a) Xét dấu tam thức (Nhận biết)
            ########################################################################
            # Tạo bảng xét dấu bằng tabular
            table_true = ('''\\begin{tabular}{|c|ccccccc|}
            \\hline
            $x$ & $-\\infty$ & & %s & & %s & & $+\\infty$ \\\\
            \\hline
            $f(x)$ & & $-$ & $0$ & $+$ & $0$ & $-$ & \\\\
            \\hline
            \\end{tabular}''' % (latex(x1), latex(x2)))

            table_false = ('''\\begin{tabular}{|c|ccccccc|}
            \\hline
            $x$ & $-\\infty$ & & %s & & %s & & $+\\infty$ \\\\
            \\hline
            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & \\\\
            \\hline
            \\end{tabular}''' % (latex(x1), latex(x2)))

            nb_da_1_d = '\\True Tam thức bậc hai $f(x)$ có bảng xét dấu như sau: \\\\ ' + table_true
            nb_da_1_s = 'Tam thức bậc hai $f(x)$ có bảng xét dấu như sau: \\\\ ' + table_false
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Tam thức $f(x) = %s$ có hai nghiệm phân biệt $x_1 = %s, x_2 = %s$. 
                            Vì hệ số $a = -1 < 0$ nên $f(x)$ dương trong khoảng hai nghiệm và âm ngoài khoảng hai nghiệm.''' 
                            % (latex(f_x), latex(x1), latex(x2)))

            ########################################################################
            # b) Luôn âm/dương (Thông hiểu)
            ########################################################################
            th_da_1_d = 'Tam thức bậc hai $f(x)$ luôn âm với mọi $x \\in \\mathbb{R}$'
            th_da_1_s = 'Tam thức bậc hai $f(x)$ luôn dương với mọi $x \\in \\mathbb{R}$'
            # Cả hai đều sai vì tam thức có 2 nghiệm, nhưng ta chọn ngẫu nhiên để làm phương án nhiễu
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Vì $\\Delta = b^2 - 4ac = (%s)^2 - 4(-1)(%s) = %s > 0$ nên tam thức luôn có khoảng dương và khoảng âm, 
                            khẳng định $f(x)$ luôn âm hoặc luôn dương là sai.''' 
                            % (latex(b_coeff), latex(c_coeff), latex(b_coeff**2 - 4*a_coeff*c_coeff)))

            ########################################################################
            # c) Tập nghiệm bất phương trình (Vận dụng)
            ########################################################################
            # S là tập f(x) < 0 => S = (-inf, x1) U (x2, +inf)
            k_val = x2 + random.randint(1, 5)
            vd_da_1_d = '\\True Gọi $S$ là tập nghiệm của bất phương trình $f(x) < 0$. Khi đó $(%s; 2026)$ là tập con của $S$' % (latex(k_val))
            vd_da_1_s = 'Gọi $S$ là tập nghiệm của bất phương trình $f(x) < 0$. Khi đó $(%s; %s)$ là tập con của $S$' % (latex(x1), latex(x2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $f(x) < 0 \\Leftrightarrow x \\in (-\\infty; %s) \\cup (%s; +\\infty)$. 
                            Vậy $S = (-\\infty; %s) \\cup (%s; +\\infty)$. 
                            Dễ thấy với $k > %s$ thì $(k; 2026) \\subset (%s; +\\infty) \\subset S$.''' 
                            % (latex(x1), latex(x2), latex(x1), latex(x2), latex(x2), latex(x2)))

            ########################################################################
            # d) Độ dài tập nghiệm (Vận dụng cao)
            ########################################################################
            length_val = x2 - x1
            vdc_da_1_d = '\\True Bất phương trình $\\frac{f(x)}{x^2 + 2} \\ge 0$ có độ dài tập nghiệm bằng $%s$' % (latex(length_val))
            vdc_da_1_s = 'Bất phương trình $\\frac{f(x)}{x^2 + 2} \\ge 0$ có độ dài tập nghiệm bằng $%s$' % (latex(length_val + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Vì $x^2 + 2 > 0$ với mọi $x \\in \\mathbb{R}$ nên: \\\\
                            $\\frac{f(x)}{x^2 + 2} \\ge 0 \\Leftrightarrow f(x) \\ge 0 \\Leftrightarrow %s \\le x \\le %s$. \\\\
                            Tập nghiệm là $T = [%s; %s]$. Độ dài tập nghiệm là $L = %s - (%s) = %s$.''' 
                            % (latex(x1), latex(x2), latex(x1), latex(x2), latex(x2), latex(x1), latex(length_val)))

            ########################################################################
            # Xử lý chọn số lượng đáp án đúng (1-3)
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng (trong bài này các lời giải được viết tĩnh theo logic biến số)
            # Để đơn giản và chính xác, ta xuất nội dung theo thứ tự a, b, c, d
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

