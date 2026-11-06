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


def bt_dang14_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Các thông số cố định theo đề bài
            a1 = 2
            b1 = 3
            # Biểu thức I
            f_I = (a1 * (sqrt(b1*x + 1) - 1)) / x
            I_val = limit(f_I, x, 0)

            # Biểu thức J
            # x^2 - x - 2 = (x + 1)(x - 2)
            tu_J = x**2 - x - 2
            mau_J = x + 1
            f_J = tu_J / mau_J
            J_val = limit(f_J, x, -1)

            # Kết quả cuối cùng
            ket_qua = I_val - J_val

            # Đáp án trắc nghiệm (Giả lập các đáp án sai quanh kết quả đúng)
            da_d = '\\True $%s$' % latex(ket_qua)
            s = [
                '$%s$' % latex(ket_qua + 1),
                '$%s$' % latex(ket_qua - 2),
                '$%s$' % latex(ket_qua * 2)
            ]
            random.shuffle(s)
            list_ans = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho $I = \lim_{x \to 0} \frac{%s(\sqrt{%sx+1}-1)}{x}$ và $J = \lim_{x \to -1} \frac{%s}{%s}$. Giá trị $I - J$ bằng''' % (
                latex(a1), latex(b1), latex(tu_J), latex(mau_J)
            )

            # Nội dung lời giải
            loigiai = r'''Ta có:
            $I = \lim_{x \to 0} \frac{%s(\sqrt{%sx+1}-1)}{x} = \lim_{x \to 0} \frac{%sx}{x(\sqrt{%sx+1}+1)} = \lim_{x \to 0} \frac{%s}{\sqrt{%sx+1}+1} = %s$. \\
            $J = \lim_{x \to -1} \frac{x^2 - x - 2}{x+1} = \lim_{x \to -1} \frac{(x+1)(x-2)}{x+1} = \lim_{x \to -1} (x-2) = %s$. \\
            Khi đó $I - J = %s - (%s) = %s$.''' % (
                latex(a1), latex(b1), latex(a1*b1), latex(b1), latex(a1*b1), latex(b1), latex(I_val),
                latex(J_val), latex(I_val), latex(J_val), latex(ket_qua)
            )

            # Xuất kết quả
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choice \n'
                '{' + list_ans[0] + '}\n'
                '{' + list_ans[1] + '}\n'
                '{' + list_ans[2] + '}\n'
                '{' + list_ans[3] + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n')
            return content

