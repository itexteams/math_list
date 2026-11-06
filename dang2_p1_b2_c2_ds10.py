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


def bt_dang2_p1_b2_c2_ds10(self):
            # Khai báo biến
            x,y=symbols('x y')
            # Tạo các hệ số a1, b1, c1, a2, b2, c2 ngẫu nhiên
            a1, b1, c1 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
            while a1 == b1:
                a1, b1, c1 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
            a2, b2, c2 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
            while a2 == b2:
                a2, b2, c2 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)

            # Thiết lập điểm (x0, y0) sao cho thỏa mãn điều kiện của miền nghiệm
            x0, y0 = random.randint(-9, 9), random.randint(-9, 9)
            while a1 * x0 + b1 * y0 + c1 <= 0 or a2 * x0 + b2 * y0 + c2 >= 0:
                x0, y0 = random.randint(-9, 9), random.randint(-9, 9)

            # Tạo các điểm (x1, y1), (x2, y2), (x3, y3) không thuộc miền nghiệm
            x1, y1 = random.randint(-9, 9), random.randint(-9, 9)
            while a1 * x1 + b1 * y1 + c1 > 0 and a2 * x1 + b2 * y1 + c2 < 0:
                x1, y1 = random.randint(-9, 9), random.randint(-9, 9)

            x2, y2 = random.randint(-9, 9), random.randint(-9, 9)
            while a1 * x2 + b1 * y2 + c1 > 0 and a2 * x2 + b2 * y2 + c2 < 0:
                x2, y2 = random.randint(-9, 9), random.randint(-9, 9)

            x3, y3 = random.randint(-9, 9), random.randint(-9, 9)
            while a1 * x3 + b1 * y3 + c1 > 0 and a2 * x3 + b2 * y3 + c2 < 0:
                x3, y3 = random.randint(-9, 9), random.randint(-9, 9)

            #Nội dung câu hỏi
            noidungcauhoi = ('Cho hệ bất phương trình bậc nhất hai ẩn $\\heva{& %s \\\\ & %s}$. Cặp số nào dưới đây là một nghiệm của hệ? \n' 
                            %(latex(a1*x +b1* y +c1 > 0),latex(a2*x +b2*y +c2 < 0))
                            )
            # Các đáp án
            da_d = '\\True $(%s;%s)$'%(latex(x0),latex(y0))
            da_s1 = '$(%s;%s)$'%(latex(x1),latex(y1))
            da_s2 = '$(%s;%s)$'%(latex(x2),latex(y2))
            da_s3 = '$(%s;%s)$'%(latex(x3),latex(y3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=('Cặp số $(%s;%s)$ thỏa mãn cả hai bất phương trình của hệ nên nó là một nghiệm của hệ bất phương trình bậc nhất hai ẩn đã cho.'
                    %(latex(x0),latex(y0)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n') 
            return content

