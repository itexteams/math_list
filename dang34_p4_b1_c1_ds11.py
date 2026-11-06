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


def bt_dang34_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                # Random tử số và mẫu số của góc alpha để tạo ra nhiều bài toán khác nhau độc lập với kết quả
                # Đảm bảo mẫu số khác 0 và phân số tối giản
                n = random.choice([5, 6, 7, 8, 9, 11, 12])
                m = n + random.choice([-1, 1, 2, -2])

                # Kết quả cuối cùng luôn là số nguyên bằng 3
                kq_so = 3
                da = '$%s$' % (kq_so)

                # Tạo các phương án sai ngẫu nhiên loại trừ đáp án đúng
                s = ['$0$', '$1$', '$2$', '$4$', '$5$', '$-3$']
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi theo format đề bài
                noidungcauhoi = ('''Tính giá trị biểu thức $M = \\sqrt{\\sin^4 \\alpha + 4\\cos^2 \\alpha} + \\sqrt{\\cos^4 \\alpha + 4\\sin^2 \\alpha}$ khi $\\alpha = \\frac{%s}{%s}\\pi$.'''
                                 %(latex(m), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên danh sách phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước không viết tắt
                loigiai=('''Ta biến đổi các biểu thức dưới dấu căn thức như sau:\\\\
                         Xét căn thức thứ nhất:\\\\
                         $\\sqrt{\\sin^4 \\alpha + 4\\cos^2 \\alpha} = \\sqrt{\\sin^4 \\alpha + 4(1 - \\sin^2 \\alpha)} = \\sqrt{\\sin^4 \\alpha - 4\\sin^2 \\alpha + 4} = \\sqrt{(\\sin^2 \\alpha - 2)^2}$.\\\\
                         Vì $0 \\le \\sin^2 \\alpha \\le 1$ với mọi $\\alpha$ nên $\\sin^2 \\alpha - 2 < 0$, suy ra:\\\\
                         $\\sqrt{(\\sin^2 \\alpha - 2)^2} = |\\sin^2 \\alpha - 2| = 2 - \\sin^2 \\alpha$.\\\\
                         Xét căn thức thứ hai:\\\\
                         $\\sqrt{\\cos^4 \\alpha + 4\\sin^2 \\alpha} = \\sqrt{\\cos^4 \\alpha + 4(1 - \\cos^2 \\alpha)} = \\sqrt{\\cos^4 \\alpha - 4\\cos^2 \\alpha + 4} = \\sqrt{(\\cos^2 \\alpha - 2)^2}$.\\\\
                         Vì $0 \\le \\cos^2 \\alpha \\le 1$ với mọi $\\alpha$ nên $\\cos^2 \\alpha - 2 < 0$, suy ra:\\\\
                         $\\sqrt{(\\cos^2 \\alpha - 2)^2} = |\\cos^2 \\alpha - 2| = 2 - \\cos^2 \\alpha$.\\\\
                         Thay hai kết quả thu gọn vào biểu thức $M$, ta thu được:\\\\
                         $M = (2 - \\sin^2 \\alpha) + (2 - \\cos^2 \\alpha) = 4 - (\\sin^2 \\alpha + \\cos^2 \\alpha)$.\\\\
                         Mà ta luôn có hệ thức cơ bản $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$, do đó:\\\\
                         $M = 4 - 1 = 3$.\\\\
                         Như vậy, giá trị của biểu thức $M$ là một hằng số độc lập với biến $\\alpha$.\\\\
                         Do đó, với $\\alpha = \\frac{%s}{%s}\\pi$ thì giá trị của $M$ vẫn bằng $3$.'''
                         %(latex(m), latex(n)))

            # Xuất câu trắc nghiệm đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

