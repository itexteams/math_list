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


def bt_dang18_p2_b2_c3_ds12(self):
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Để giữ tính chất bài toán (nguyên hàm x^4), ta giữ hệ số 4 của x^3.
            # Thay đổi tham số n trong f(x) = 4x^3 + n*x
            n = random.randint(1, 5) 
            f = 4*x**3 + n*x

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x) = %s$ liên tục trên $\mathbb{R}$.''' % (latex(f))

            ########################################################################
            # Nhận biết - Câu a: Tính tích phân cơ bản
            ########################################################################
            low_a, high_a = 3, 5
            val_a = integrate(f, (x, low_a, high_a))

            da_a_d = r'\True $\int_{%s}^{%s} (%s) \text{d}x = %s$.' % (low_a, high_a, latex(f), latex(val_a))
            da_a_s = r'$\int_{%s}^{%s} (%s) \text{d}x = %s$.' % (low_a, high_a, latex(f), latex(val_a + random.randint(1, 10)))

            list_da_a = [da_a_d, da_a_s]
            shuffled_da_a = random.choice(list_da_a)
            loigiai_a = r'Ta có: $\int_{%s}^{%s} (%s) \text{d}x = %s$.' % (low_a, high_a, latex(f), latex(val_a))

            ########################################################################
            # Thông hiểu - Câu b: Tìm nguyên hàm thỏa điều kiện
            ########################################################################
            # F(1) = 4. Tính F(2)
            # F_basic là nguyên hàm không có C
            F_basic = x**4 + Rational(n, 2)*x**2
            C_val = 4 - F_basic.subs(x, 1)
            F_x = F_basic + C_val
            val_b = F_x.subs(x, 2)

            da_b_d = r'\True Cho $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(1)=4$. Khi đó $F(2) = %s$.' % (latex(val_b))
            da_b_s = r'Cho $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(1)=4$. Khi đó $F(2) = %s$.' % (latex(val_b - 1))

            list_da_b = [da_b_d, da_b_s]
            shuffled_da_b = random.choice(list_da_b)

            loigiai_b = r'''$F(x) = \int f(x) \text{d}x = \int (%s) \text{d}x = x^4 + \frac{%sx^2}{2} + C$ \\
            $F(1) = 4 \Rightarrow 1^4 + \frac{%s \cdot 1^2}{2} + C = 4 \Rightarrow C = %s$ \\
            $\Rightarrow F(x) = x^4 + \frac{%sx^2}{2} + %s$ \\
            $\Rightarrow F(2) = 2^4 + \frac{%s \cdot 2^2}{2} + %s = %s$.''' % (
                latex(f), n, n, latex(C_val), n, latex(C_val), n, latex(C_val), latex(val_b)
            )

            ########################################################################
            # Vận dụng - Câu c: Tích phân tổng hợp
            ########################################################################
            # Tính tích phân từ 0 đến 2 của (1 + 2x + f(x))
            expr_c = 1 + 2*x + f
            val_c = integrate(expr_c, (x, 0, 2))

            da_c_d = r'\True $\int_{0}^{2} (1 + 2x + f(x)) \text{d}x = %s$.' % (latex(val_c))
            da_c_s = r'$\int_{0}^{2} (1 + 2x + f(x)) \text{d}x = %s$.' % (latex(val_c + 2))

            list_da_c = [da_c_d, da_c_s]
            shuffled_da_c = random.choice(list_da_c)

            loigiai_c = r'''$\int_{0}^{2} (1 + 2x + f(x)) \text{d}x = \int_{0}^{2} (1 + 2x + 4x^3 + %sx) \text{d}x = \int_{0}^{2} (4x^3 + %sx + 1) \text{d}x$ \\
            $= \left( x^4 + \frac{%s}{2}x^2 + x \right) \bigg|_{0}^{2} = \left( 2^4 + \frac{%s}{2} \cdot 2^2 + 2 \right) - 0 = %s$.''' % (
                n, n + 2, n + 2, n + 2, latex(val_c)
            )

            ########################################################################
            # Vận dụng cao - Câu d: Tích phân chứa dấu trị tuyệt đối
            ########################################################################
            # Tính tích phân từ -2 đến 1 của |f(x)|
            # Vì f(x) = x(4x^2 + n) và n > 0 nên f(x) đổi dấu qua x = 0
            val_d_part1 = integrate(-f, (x, -2, 0))
            val_d_part2 = integrate(f, (x, 0, 1))
            val_d = val_d_part1 + val_d_part2

            da_d_d = r'\True $\int_{-2}^{1} |f(x)| \text{d}x = %s$.' % (latex(val_d))
            da_d_s = r'$\int_{-2}^{1} |f(x)| \text{d}x = %s$.' % (latex(val_d - Rational(1, 2)))

            list_da_d = [da_d_d, da_d_s]
            shuffled_da_d = random.choice(list_da_d)

            loigiai_d = r'''$\int_{-2}^{1} |f(x)| \text{d}x = \int_{-2}^{1} |4x^3 + %sx| \text{d}x = \int_{-2}^{0} (-4x^3 - %sx) \text{d}x + \int_{0}^{1} (4x^3 + %sx) \text{d}x$ \\
            $= %s + %s = %s$.''' % (
                n, n, n, latex(val_d_part1), latex(val_d_part2), latex(val_d)
            )

            # Kiểm tra số câu đúng (từ 1 đến 3) - Logic này có thể mở rộng nếu bạn có nhiều phương án sai hơn
            # Ở đây mỗi câu đang chọn ngẫu nhiên giữa Đúng và Sai.

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + shuffled_da_a + '}\n'
                '{' + shuffled_da_b + '}\n'
                '{' + shuffled_da_c + '}\n'
                '{' + shuffled_da_d + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_a + '\n'
                '\\item ' + loigiai_b + '\n'
                '\\item ' + loigiai_c + '\n'
                '\\item ' + loigiai_d + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

