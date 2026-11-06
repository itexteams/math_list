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


def bt_dang12_p4_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo các ký hiệu toán học
            a, b = symbols('a b', positive=True)


            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                x_val = random.randint(2, 4)
                y_val = random.randint(2, 4)
                z_val = random.randint(5, 10)

                m = Rational(1, x_val)
                n = Rational(1, y_val)
                k = Rational(1, z_val)

                # Tính các số mũ ở tử số
                m_plus_k = m + k
                n_plus_k = n + k

                # Hàm hỗ trợ hiển thị căn thức hoặc lũy thừa đẹp
                def format_exp(var, expo):
                    if expo == Rational(1, 2):
                        return r"\sqrt{%s}" % var
                    if expo.numerator == 1:
                        return r"\sqrt[%s]{%s}" % (expo.denominator, var)
                    return r"{%s}^{%s}" % (var, latex(expo))

                # Chuẩn bị nội dung hiển thị cho đề bài
                # Ta xen kẽ giữa cách viết lũy thừa và căn thức như ảnh mẫu
                term1 = r"{%s}^{%s} %s" % (latex(a), latex(m), format_exp('b', n_plus_k))
                term2 = r"{%s}^{%s} %s" % (latex(b), latex(n), format_exp('a', m_plus_k))
                denom = r"%s + %s" % (format_exp('a', k), format_exp('b', k))

                bieu_thuc_A = r"\frac{%s + %s}{%s}" % (term1, term2, denom)

                # Kết quả
                tich_mn = m * n
                da = '$%s$' % latex(tich_mn)

                # Tạo các đáp án nhiễu
                s = [
                    '$%s$' % latex(m + n),
                    '$%s$' % latex(Rational(1, x_val + y_val)),
                    '$%s$' % latex(m * n * 2),
                    '$%s$' % latex(m / n if n != 0 else m),
                    '$%s$' % latex(Rational(1, x_val * y_val + 1)),
                    '$1$'
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách nhiễu
                if da in s: s.remove(da)

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = (r"Cho hai số thực dương $a, b$. Rút gọn biểu thức $A = %s$ ta thu được $A = a^m \cdot b^n$. Tính tích $m.n$." 
                                 % bieu_thuc_A)

                # Đáp án trắc nghiệm
                da_d = r'\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết
                # Bước biến đổi tử số: đặt a^m.b^n ra ngoài
                loigiai = (r"Biến đổi biểu thức $A$ về dạng lũy thừa: \\ "
                           r"$A = \frac{a^{%s}b^{%s} + b^{%s}a^{%s}}{a^{%s} + b^{%s}} $ \\ "
                           r"$A = \frac{a^{%s}b^{%s}(b^{%s} + a^{%s})}{a^{%s} + b^{%s}} $ \\ "
                           r"$A = a^{%s}b^{%s}$. \\ "
                           r"Suy ra $m = %s, n = %s \Rightarrow m.n = %s$."
                           % (latex(m), latex(n_plus_k), latex(n), latex(m_plus_k), latex(k), latex(k),
                              latex(m), latex(n), latex(k), latex(k), latex(k), latex(k),
                              latex(m), latex(n), latex(m), latex(n), latex(tich_mn)))

            # Xuất nội dung theo định dạng LaTeX mong muốn
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

