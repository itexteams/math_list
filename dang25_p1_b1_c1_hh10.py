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


def bt_dang25_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến: Tập hợp các đẳng thức đúng và sai cùng lời giải tương ứng
            true_pool = {
                '\\sin 45^\\circ + \\sin 45^\\circ = \\sqrt{2}': '\\sin 45^\\circ + \\sin 45^\\circ = \\frac{\\sqrt{2}}{2} + \\frac{\\sqrt{2}}{2} = \\sqrt{2}',
                '\\sin 30^\\circ + \\cos 60^\\circ = 1': '\\sin 30^\\circ + \\cos 60^\\circ = \\frac{1}{2} + \\frac{1}{2} = 1',
                '\\sin 60^\\circ + \\cos 150^\\circ = 0': '\\sin 60^\\circ + \\cos 150^\\circ = \\frac{\\sqrt{3}}{2} + \\left(-\\frac{\\sqrt{3}}{2}\\right) = 0',
                '\\sin 135^\\circ + \\cos 135^\\circ = 0': '\\sin 135^\\circ + \\cos 135^\\circ = \\frac{\\sqrt{2}}{2} + \\left(-\\frac{\\sqrt{2}}{2}\\right) = 0',
                '\\sin 150^\\circ + \\cos 120^\\circ = 0': '\\sin 150^\\circ + \\cos 120^\\circ = \\frac{1}{2} + \\left(-\\frac{1}{2}\\right) = 0',
                '\\cos 30^\\circ + \\sin 120^\\circ = \\sqrt{3}': '\\cos 30^\\circ + \\sin 120^\\circ = \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{3}}{2} = \\sqrt{3}'
            }

            false_pool = {
                '\\sin 120^\\circ + \\cos 30^\\circ = 0': '\\sin 120^\\circ + \\cos 30^\\circ = \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{3}}{2} = \\sqrt{3} \\neq 0',
                '\\sin 45^\\circ + \\cos 45^\\circ = 1': '\\sin 45^\\circ + \\cos 45^\\circ = \\frac{\\sqrt{2}}{2} + \\frac{\\sqrt{2}}{2} = \\sqrt{2} \\neq 1',
                '\\sin 60^\\circ + \\cos 30^\\circ = 0': '\\sin 60^\\circ + \\cos 30^\\circ = \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{3}}{2} = \\sqrt{3} \\neq 0',
                '\\cos 120^\\circ + \\sin 150^\\circ = 1': '\\cos 120^\\circ + \\sin 150^\\circ = -\\frac{1}{2} + \\frac{1}{2} = 0 \\neq 1'
            }

            # Chọn ngẫu nhiên 1 đẳng thức sai (đây chính là đáp án cần tìm vì đề hỏi "Đẳng thức nào sai")
            false_key = random.choice(list(false_pool.keys()))
            da = false_key

            # Chọn ngẫu nhiên 3 đẳng thức đúng (các phương án nhiễu)
            true_keys = random.sample(list(true_pool.keys()), 3)
            das1 = true_keys[0]
            das2 = true_keys[1]
            das3 = true_keys[2]

            # Câu hỏi
            noidungcauhoi = ('%s' % ('Đẳng thức nào sau đây sai?'))

            # Các đáp án
            da_d = ('\\True $%s$' % (da))
            da_s1 = ('$%s$' % (das1))
            da_s2 = ('$%s$' % (das2))
            da_s3 = ('$%s$' % (das3))

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Ta kiểm tra từng phương án: \\\\
                +) $%s$. \\\\
                +) $%s$. \\\\
                +) $%s$. \\\\
                +) $%s$. \\\\
                Vậy đẳng thức sai là $%s$.''' % (
                true_pool[das1],
                true_pool[das2],
                true_pool[das3],
                false_pool[da],
                da
            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '{'+str(list_1[0])+'}\n'
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

