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


def bt_dang9_p1_b1_c1_ds11(self):
            # Khai báo biến
            i=randint(1,100)
            k=2*i+1
            lis1=[30*k,-30*k,45*k,-45*k,60*k,-60*k]
            goc=random.choice(lis1)
            goc_rad=goc * pi / 180
            lis=['1','2','3','4','5','6','7','8']
            dang=random.choice(lis)

            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\sin \\left(%s\\right)$ bằng \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(sin(goc_rad)))
                da_s1 = '$%s$'%(latex(sin(goc_rad+pi/5)))
                da_s2 = '$%s$'%(latex(sin(goc_rad+pi/7)))
                da_s3 = '$%s$'%(latex(sin(goc_rad-pi/9)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\sin \\left(%s\\right)=%s$.'%(latex(goc_rad), latex(sin(goc_rad)))
                        )
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\cos \\left(%s\\right)$ bằng \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = ' $%s$'%(latex(cos(goc_rad+pi/4)))
                da_s1 = '\\True $%s$'%(latex(cos(goc_rad)))
                da_s2 = '$%s$'%(latex(cos(goc_rad+pi/3)))
                da_s3 = '$%s$'%(latex(cos(goc_rad-pi/6)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\cos \\left(%s\\right)=%s$.'%(latex(goc_rad), latex(cos(goc_rad)))
                        )
            if dang=='7':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\tan \\left(%s\\right)$ bằng \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = ' $%s$'%(latex(tan(goc_rad+pi/4)))
                da_s1 = ' $%s$'%(latex(tan(goc_rad+pi/6)))
                da_s2 = '\\True $%s$'%(latex(tan(goc_rad)))
                da_s3 = '$%s$'%(latex(tan(goc_rad-pi/3)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\tan \\left(%s\\right)=%s$.'%(latex(goc_rad), latex(tan(goc_rad)))
                        )
            if dang=='8':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\cot \\left(%s\\right)$ bằng \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = ' $%s$'%(latex(cot(goc_rad+pi/4)))
                da_s1 = ' $%s$'%(latex(cot(goc_rad+pi/3)))
                da_s2 = ' $%s$'%(latex(cot(goc_rad-pi/6)))
                da_s3 = '\\True $%s$'%(latex(cot(goc_rad)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\cot \\left(%s\\right)=%s$.'%(latex(goc_rad), latex(cot(goc_rad)))
                        )

            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\sin \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(goc))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(sin(goc_rad)))
                da_s1 = '$%s$'%(latex(sin(goc_rad+pi/4)))
                da_s2 = '$%s$'%(latex(sin(goc_rad+pi/3)))
                da_s3 = '$%s$'%(latex(sin(goc_rad-pi/6)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\sin \\left(%s^\\circ \\right)=%s$.'%(latex(goc), latex(sin(goc_rad)))
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\cos \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(goc))
                            )
                # Các đáp án
                da_d = ' $%s$'%(latex(cos(goc_rad+pi/4)))
                da_s1 = '\\True $%s$'%(latex(cos(goc_rad)))
                da_s2 = '$%s$'%(latex(cos(goc_rad+pi/3)))
                da_s3 = '$%s$'%(latex(cos(goc_rad-pi/6)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\cos \\left(%s^\\circ \\right)=%s$.'%(latex(goc), latex(cos(goc_rad)))
                        )
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\tan \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(goc))
                            )
                # Các đáp án
                da_d = ' $%s$'%(latex(tan(goc_rad+pi/4)))
                da_s1 = ' $%s$'%(latex(tan(goc_rad+pi/6)))
                da_s2 = '\\True $%s$'%(latex(tan(goc_rad)))
                da_s3 = '$%s$'%(latex(tan(goc_rad-pi/3)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\tan \\left(%s^\\circ \\right)=%s$.'%(latex(goc), latex(tan(goc_rad)))
                        )
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $\\cot \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(goc))
                            )
                # Các đáp án
                da_d = ' $%s$'%(latex(cot(goc_rad+pi/4)))
                da_s1 = ' $%s$'%(latex(cot(goc_rad+pi/3)))
                da_s2 = ' $%s$'%(latex(cot(goc_rad-pi/6)))
                da_s3 = '\\True $%s$'%(latex(cot(goc_rad)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\cot \\left(%s^\\circ \\right)=%s$.'%(latex(goc), latex(cot(goc_rad)))
                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('=\\tilde{\\infty}','\\text{ là không xác định}').replace('\\tilde{\\infty}','\\text{Không xác định}')
            return content

