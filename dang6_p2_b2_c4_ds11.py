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


def bt_dang6_p2_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số để tạo bài toán mới
            # a: điểm tới hạn (ví dụ từ 2 đến 5)
            # k: hằng số ở tử số g(x) (ví dụ từ 1 đến 5)
            a = random.randint(2, 9)
            k = random.randint(1, 9)

            # Định nghĩa các biểu thức để dùng latex
            f_expr = x / Abs(x - a)
            g_expr = (x - k) / (x**2)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho 2 hàm số $f(x)=%s$ và $g(x)=%s$.''' 
                             % (latex(f_expr), latex(g_expr)))

            ########################################################################
            # Nhận biết: Giới hạn f(x) khi x -> a+
            ########################################################################
            nb_da_1_d = r'\True Khi $x \to %s^+$, ta có $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} \frac{x}{x-%s}$' % (a, a, a, a)
            nb_da_1_s = r'Khi $x \to %s^+$, ta có $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} \frac{x}{-x+%s}$' % (a, a, a, a)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Khi $x \to %s^+$ ta có $x - %s > 0 \Rightarrow |x - %s| = x - %s$. \\ Do đó $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} \frac{x}{x-%s}$.''' 
                            % (a, a, a, a, a, a, a))

            ########################################################################
            # Thông hiểu: Giới hạn g(x) khi x -> 0
            ########################################################################
            th_da_1_d = r'\True Giới hạn $\lim_{x \to 0} g(x) = -\infty$'
            th_da_1_s = r'Giới hạn $\lim_{x \to 0} g(x) = +\infty$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Vì $\lim_{x \to 0}(x-%s) = -%s < 0$; $\lim_{x \to 0} x^2 = 0$ và $x^2 > 0$ khi $x \to 0$. \\ Do đó $\lim_{x \to 0} g(x) = \lim_{x \to 0} \frac{x-%s}{x^2} = -\infty$.''' 
                            % (k, k, k))

            ########################################################################
            # Vận dụng: Giới hạn f(x) khi x -> a-
            ########################################################################
            vd_da_1_d = r'\True Giới hạn $\lim_{x \to %s^-} f(x) = +\infty$' % (a)
            vd_da_1_s = r'Giới hạn $\lim_{x \to %s^-} f(x) = -\infty$' % (a)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Khi $x \to %s^-$ thì $|x - %s| = -x + %s$. \\ Vì $\lim_{x \to %s^-} x = %s > 0$; $\lim_{x \to %s^-} (-x + %s) = 0$ và $-x + %s > 0$ khi $x \to %s^-$. \\ Nên $\lim_{x \to %s^-} f(x) = \lim_{x \to %s^-} \frac{x}{-x+%s} = +\infty$.''' 
                            % (a, a, a, a, a, a, a, a, a, a, a, a))

            ########################################################################
            # Vận dụng cao: Giới hạn tích f(x).g(x) khi x -> 0+
            ########################################################################
            vdc_da_1_d = r'\True Giới hạn $\lim_{x \to 0^+} [f(x) \cdot g(x)] = -\infty$'
            vdc_da_1_s = r'Giới hạn $\lim_{x \to 0^+} [f(x) \cdot g(x)] = +\infty$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Ta có $\lim_{x \to 0^+} [f(x) \cdot g(x)] = \lim_{x \to 0^+} \left[ \frac{x}{|x-%s|} \cdot \frac{x-%s}{x^2} \right] = \lim_{x \to 0^+} \frac{1}{x} \cdot \frac{x-%s}{|x-%s|}$. \\ $\lim_{x \to 0^+} \frac{x-%s}{|x-%s|} = \frac{-%s}{%s}$ và $\lim_{x \to 0^+} \frac{1}{x} = +\infty$. \\ Nên $\lim_{x \to 0^+} \frac{1}{x} \cdot \frac{x-%s}{|x-%s|} = -\infty$.''' 
                             % (a, k, k, a, k, a, k, a, k, a))

            # Hàm đếm số câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp xáo trộn để đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

