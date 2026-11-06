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


def bt_dang35_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tiến hành random góc alpha = m/n * pi để tạo ra nhiều câu hỏi khác nhau
                n = random.choice([5, 6, 7, 8, 9, 11, 12])
                m = n + random.choice([-2, -1, 1, 2])

                # Kết quả cuối cùng là hằng số nguyên
                kq_so = 3
                da = '$%s$' % (kq_so)

                # Tạo các phương án sai ngẫu nhiên đảm bảo không trùng với đáp án đúng
                s = ['$0$', '$1$', '$2$', '$4$', '$5$', '$-3$']
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Đề bài thu được từ image_1a3f4e.png
                noidungcauhoi = ('''Tính giá trị biểu thức $N = \\sin^2 \\alpha \\cdot \\tan^2 \\alpha + 4\\sin^2 \\alpha - \\tan^2 \\alpha + 3\\cos^2 \\alpha$ khi $\\alpha = \\frac{%s}{%s}\\pi$.'''
                                 %(latex(m), latex(n)))

                # Các phương án trả lời theo định dạng mẫu
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên vị trí các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, rõ ràng từng bước
                loigiai=('''Ta tiến hành thu gọn biểu thức $N$ bằng cách nhóm các hạng tử phù hợp:\\\\
                         $N = \\left(\\sin^2 \\alpha \\cdot \\tan^2 \\alpha - \\tan^2 \\alpha\\right) + 4\\sin^2 \\alpha + 3\\cos^2 \\alpha$\\\\
                         $N = \\tan^2 \\alpha \\cdot \\left(\\sin^2 \\alpha - 1\\right) + 4\\sin^2 \\alpha + 3\\cos^2 \\alpha$.\\\\
                         Áp dụng hệ thức lượng giác cơ bản $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$, ta suy ra $\\sin^2 \\alpha - 1 = -\\cos^2 \\alpha$. Thay vào biểu thức ta được:\\\\
                         $N = \\tan^2 \\alpha \\cdot \\left(-\\cos^2 \\alpha\\right) + 4\\sin^2 \\alpha + 3\\cos^2 \\alpha$\\\\
                         $N = -\\frac{\\sin^2 \\alpha}{\\cos^2 \\alpha} \\cdot \\cos^2 \\alpha + 4\\sin^2 \\alpha + 3\\cos^2 \\alpha$\\\\
                         $N = -\\sin^2 \\alpha + 4\\sin^2 \\alpha + 3\\cos^2 \\alpha$\\\\
                         $N = 3\\sin^2 \\alpha + 3\\cos^2 \\alpha$\\\\
                         $N = 3\\left(\\sin^2 \\alpha + \\cos^2 \\alpha\\right) = 3 \\cdot 1 = 3$.\\\\
                         Như vậy, giá trị của biểu thức $N$ luôn bằng $3$ với mọi góc $\\alpha$.\\\\
                         Do đó, khi $\\alpha = \\frac{%s}{%s}\\pi$ thì giá trị biểu thức $N$ vẫn bằng $3$.'''
                         %(latex(m), latex(n)))

            # Xuất câu trắc nghiệm đúng khung chương trình
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

