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


def bt_dang3_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Để giữ đúng tính chất bài toán mẫu (nghiệm kép x=b/a và nghiệm đơn x=1):
            # Ta chọn cấu trúc: f(x) = (ax - b) * (ax^2 - (a+b)x + b)
            while True:
                a = random.randint(2, 5)
                b = random.randint(1, 10)
                if sp.gcd(a, b) == 1 and b/a < 1: # Đảm bảo phân số tối giản và b/a < 1 như đề mẫu
                    break

            f1 = a*x - b
            f2 = a*x**2 - (a+b)*x + b
            expr1_tex = latex(f1)
            expr2_tex = latex(f2)
            r_min = Rational(b, a)
            r_max = Rational(1, 1)

            # Nội dung câu hỏi
            noidungcauhoi = r"Cho biểu thức $f(x) = (%s)(%s)$." % (expr1_tex, expr2_tex)

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = r'\True $f(x)=0 \Leftrightarrow \left[\begin{aligned} & x=%s \\ & x=1 \end{aligned}\right.$' % (latex(r_min))
            nb_da_1_s = r'$f(x)=0 \Leftrightarrow \left[\begin{aligned} & x=%s \\ & x=1 \end{aligned}\right.$' % (latex(-r_min))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r"Biểu thức $f(x)=0 \Leftrightarrow \left[\begin{aligned} & %s=0 \\ & %s=0 \end{aligned}\right. \Leftrightarrow \left[\begin{aligned} & x=%s \\ & x=1 \end{aligned}\right.$." % (expr1_tex, expr2_tex, latex(r_min))

            ######################################################################## Thông hiểu ############################################
            # Bảng xét dấu cụ thể biểu thức
            loigiai_th_1 = r'''Bảng xét dấu:
            \begin{center}
            \begin{tikzpicture}
            \tkzTabInit[espcl=2,lgt=2.5]{$x$/1,$%s$/1,$%s$/1,$f(x)$/1}{$-\infty$,$%s$,$1$,$+\infty$}
            \tkzTabLine{,-,0,+,|,+}
            \tkzTabLine{,+,0,-,0,+}
            \tkzTabLine{,-,0,-,0,+}
            \end{tikzpicture}
            \end{center}''' % (expr1_tex, expr2_tex, latex(r_min))

            th_da_1_d = r'\True Bảng xét dấu của biểu thức $f(x)$ có dòng cuối cùng mang dấu âm trên khoảng $\left(-\infty; %s\right)$' % (latex(r_min))
            th_da_1_s = r'Bảng xét dấu của biểu thức $f(x)$ đổi dấu khi đi qua điểm $x = %s$' % (latex(r_min))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = r'\True $f(x) < 0$ khi $x \in \left(-\infty; %s \right) \cup \left(%s; 1\right)$' % (latex(r_min), latex(r_min))
            vd_da_1_s = r'$f(x) < 0$ khi $x \in \left(1; +\infty \right)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r"Dựa vào bảng xét dấu, ta thấy $f(x) < 0$ trên các khoảng $\left(-\infty; %s \right)$ và $\left(%s; 1\right)$." % (latex(r_min), latex(r_min))

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = r'\True Với $x \in \left(1; +\infty\right)$ thì $f(x) > 0$'
            vdc_da_1_s = r'Với $x \in \left(-\infty; %s\right)$ thì $f(x) > 0$' % (latex(r_min))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r"Dựa vào bảng xét dấu, $f(x) > 0$ khi $x > 1$."

            # Hàm đếm câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Xáo trộn và chọn bộ đáp án hợp lệ (1-3 câu đúng)
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán vào danh sách để khớp với phần xuất nội dung
            shuffled_answers_nb = [nb_da_1]; shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_answers_th = [th_da_1]; shuffled_solutions_th = [loigiai_th_1]
            shuffled_answers_vd = [vd_da_1]; shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_answers_vdc = [vdc_da_1]; shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn - Fix lỗi Syntax
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n \\end{minipage}\n\n').replace('\\frac', '\\dfrac')
            return content

