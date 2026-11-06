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


def bt_dang12_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số k (ví dụ chọn k là số chẵn từ 2 đến 8 để bài toán giống mẫu)
            k = random.choice([2, 4, 6, 8])
            f = x**2 - k*x
            area_val = integrate(k*x - x**2, (x, 0, k))

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x) = %s$.''' % (latex(f)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = r'\True Hoành độ giao điểm của đồ thị hàm số $y = f(x)$ và $Ox$ là nghiệm của phương trình $f(x) = 0$'
            nb_da_1_s = r'Hoành độ giao điểm của đồ thị hàm số $y = f(x)$ và $Ox$ là nghiệm của phương trình $f(x) = %s$' % (k)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'Hoành độ giao điểm của đồ thị hàm số $y = f(x)$ và $Ox$ là nghiệm của phương trình $f(x) = 0$.'
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = r'\True $%s \le 0, \forall x \in [0; %s]$ ' % (latex(f), k)
            th_da_1_s = r'$%s \ge 0, \forall x \in [0; %s]$ ' % (latex(f), k)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'Ta có $%s \le 0, \forall x \in [0; %s]$.' % (latex(f), k)
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            # Trong ảnh câu c là công thức sai (đảo cận 4-0), ta mô phỏng lại logic đó
            vd_da_1_d = r'\True Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và $Ox$ được tính theo công thức $S = \int_0^{%s} |%s| \text{d}x$' % (k, latex(f))
            vd_da_1_s = r'Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và $Ox$ được tính theo công thức $S = \int_{%s}^0 |%s| \text{d}x$' % (k, latex(f))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và $Ox$ được tính theo công thức $S = \int_0^{%s} |%s| \text{d}x$.' % (k, latex(f))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = r'\True Hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và $Ox$ có diện tích là $S = %s$' % (latex(area_val))
            vdc_da_1_s = r'Hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và $Ox$ có diện tích là $S = %s$' % (latex(area_val * 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và $Ox$ có diện tích là \\
            $S = \int_0^{%s} |%s| \text{d}x = \int_0^{%s} (%s - x^2) \text{d}x = \left( %s x^2 - \frac{x^3}{3} \right) \bigg|_0^{%s} = %s$.''' 
                            % (k, latex(f), k, k, latex(Rational(k, 2)), k, latex(area_val)))
            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Logic chọn đáp án Đúng/Sai (1-3 câu đúng)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_nb_2[0]) + '\n'
                '\\item ' + str(list_th_2[0]) + '\n'
                '\\item ' + str(list_vd_2[0]) + '\n'
                '\\item ' + str(list_vdc_2[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

