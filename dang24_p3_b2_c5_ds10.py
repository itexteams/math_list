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


def bt_dang24_p3_b2_c5_ds10(self):
            while True:
                # Chọn a, b trong khoảng nhỏ để tích giai thừa không quá lớn
                a = randint(2, 6)
                b = randint(2, 5)

                # Tính p = a! * b!
                p_val = math.factorial(a) * math.factorial(b)

                # Kiểm tra điều kiện p < 9999
                if p_val < 9999:
                    p = p_val
                    break

            # Câu hỏi
            noidungcauhoi = '''Một nhóm có $%s$ học sinh nữ và $%s$ học sinh nam. Xếp những học sinh này vào một bàn tròn sao cho nhóm học sinh nữ ngồi cạnh nhau và nhóm học sinh nam ngồi cạnh nhau. Số cách xếp bằng bao nhiêu?''' % (latex(a), latex(b))

            # Các đáp án
            da_d = '\\True $%s$' % (latex(p))

            # Tạo đáp án nhiễu thông minh hơn
            s_set = set()
            while len(s_set) < 3:
                # Các lỗi thường gặp: quên (2-1)!, hoặc tính nhầm (a+b-1)!
                offset = random.choice([2, 12, 24, 120, -2, -10])
                nhieu = p + offset
                if nhieu > 0 and nhieu != p:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_1 = [da_d] + list(s_set)
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ( 'Coi $%s$ học sinh nữ là nhóm $I$ và $%s$ học sinh nam là nhóm $II$.\\\\ \n'
                       'Số cách xếp hai nhóm $I$ và $II$ vào bàn tròn là $(2-1)! = 1$ (cách).\\\\ \n'
                       'Trong mỗi nhóm:\\\\ \n'
                       '- Số cách xếp $%s$ học sinh nữ nội bộ nhóm $I$ là $%s!$ cách.\\\\ \n'
                       '- Số cách xếp $%s$ học sinh nam nội bộ nhóm $II$ là $%s!$ cách.\\\\ \n'
                       'Theo quy tắc nhân, tổng số cách xếp thỏa mãn là: $1 \\cdot %s! \\cdot %s! = %s$ (cách).'
                       % (latex(a), latex(b),
                          latex(a), latex(a),
                          latex(b), latex(b),
                          latex(a), latex(b), latex(p))
                     )

            # Đáp án ngắn
            dapan = '\\shortans[0]{$%s$}\n' % (latex(p))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

