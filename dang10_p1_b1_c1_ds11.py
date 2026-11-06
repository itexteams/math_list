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


def bt_dang10_p1_b1_c1_ds11(self):
            # Khai báo biến
            lis0=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            a=random.choice(lis0)
            b=random.choice(lis0)
            c=random.choice(lis0)
            d=random.choice(lis0)
            e=random.choice(lis0)
            i=randint(1,100)
            k=2*i+1
            lis1=[30*k,-30*k,60*k,-60*k]
            goc1=random.choice(lis1)
            goc1_rad=goc1 * pi / 180
            goc2=random.choice(lis1)
            goc2_rad=goc2 * pi / 180
            goc3=random.choice(lis1)
            goc3_rad=goc3 * pi / 180
            goc4=random.choice(lis1)
            goc4_rad=goc4 * pi / 180
            lis2=[30*(k-1),-30*(k-1),60*(k-1),-60*(k-1)]
            goc5=random.choice(lis2)
            goc5_rad=goc5 * pi / 180
            goc6=random.choice(lis2)
            goc6_rad=goc6 * pi / 180
            kq1=a*(sin(goc1_rad))**2+b*(cos(goc2_rad))**2+c*sin(goc3_rad)+d*cos(goc4_rad)+e
            kq2=a*sin(goc1_rad)*cos(goc2_rad)+b*sin(goc3_rad)*cos(goc4_rad)
            kq3=sin(goc1_rad)*cos(goc2_rad)*sin(goc3_rad)*cos(goc4_rad)
            kq4=a*(sin(goc1_rad))**2+b*(cos(goc2_rad))**2
            kq5=a*(tan(goc5_rad))+b*(cot(goc6_rad))
            kq6=a*(sin(goc1_rad))**2+b*(cos(goc2_rad))**2+c*(tan(goc5_rad))**2+d*(cot(goc6_rad))**2
            lis=['1','2','3','4','5','6','7','8','9','10','11','12']
            dang=random.choice(lis)

            if dang=='7':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin^{2} \\left(%s \\right)+%s\\cos^{2} \\left(%s \\right)+%s\\sin \\left(%s \\right)+%s\\cos \\left(%s \\right)+%s$ bằng \n'''
                            %(latex(a),latex(goc1_rad),latex(b),latex(goc2_rad),latex(c),latex(goc3_rad),latex(d),latex(goc4_rad),latex(e))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq1))
                da_s1 = ' $%s$'%(latex(kq1+1))
                da_s2 = '$%s$'%(latex(kq1+2))
                da_s3 = '$%s$'%(latex(kq1-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq1))
                        )
            if dang=='8':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin \\left(%s \\right) \\cos \\left(%s \\right)+%s\\sin \\left(%s \\right) \\cos \\left(%s \\right)$ bằng \n'''
                            %(latex(a),latex(goc1_rad),latex(goc2_rad),latex(b),latex(goc3_rad),latex(goc4_rad))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq2))
                da_s1 = ' $%s$'%(latex(kq2+1))
                da_s2 = '$%s$'%(latex(kq2+2))
                da_s3 = '$%s$'%(latex(kq2-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq2))
                        )
            if dang=='9':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=\\sin \\left(%s \\right) \\cos \\left(%s \\right) \\sin \\left(%s \\right) \\cos \\left(%s \\right)$ bằng \n'''
                            %(latex(goc1_rad),latex(goc2_rad),latex(goc3_rad),latex(goc4_rad))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq3))
                da_s1 = ' $%s$'%(latex(kq3+1))
                da_s2 = '$%s$'%(latex(kq3+2))
                da_s3 = '$%s$'%(latex(kq3-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq3))
                        )
            if dang=='10':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin^{2} \\left(%s \\right)+%s\\cos^{2} \\left(%s \\right)$ bằng \n'''
                            %(latex(a),latex(goc1_rad),latex(b),latex(goc2_rad))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq4))
                da_s1 = ' $%s$'%(latex(kq4+1))
                da_s2 = '$%s$'%(latex(kq4+2))
                da_s3 = '$%s$'%(latex(kq4-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq4))
                        )
            if dang=='11':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\tan \\left(%s \\right)+%s\\cot \\left(%s \\right)$ bằng \n'''
                            %(latex(a),latex(goc5_rad),latex(b),latex(goc6_rad))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq5))
                da_s1 = ' $%s$'%(latex(kq5+1))
                da_s2 = '$%s$'%(latex(kq5+2))
                da_s3 = '$%s$'%(latex(kq5-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq5))
                        )
            if dang=='12':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin^{2} \\left(%s \\right)+%s\\cos^{2} \\left(%s \\right)+%s\\tan^{2} \\left(%s \\right)+%s\\cot^{2} \\left(%s \\right)$ bằng \n'''
                            %(latex(a),latex(goc1_rad),latex(b),latex(goc2_rad),latex(c),latex(goc5_rad),latex(d),latex(goc6_rad))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq6))
                da_s1 = ' $%s$'%(latex(kq6+1))
                da_s2 = '$%s$'%(latex(kq6+2))
                da_s3 = '$%s$'%(latex(kq6-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq6))
                        )

            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin^{2} \\left(%s^\\circ \\right)+%s\\cos^{2} \\left(%s^\\circ \\right)+%s\\sin \\left(%s^\\circ \\right)+%s\\cos \\left(%s^\\circ \\right)+%s$ bằng \n'''
                            %(latex(a),latex(goc1),latex(b),latex(goc2),latex(c),latex(goc3),latex(d),latex(goc4),latex(e))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq1))
                da_s1 = ' $%s$'%(latex(kq1+1))
                da_s2 = '$%s$'%(latex(kq1+2))
                da_s3 = '$%s$'%(latex(kq1-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq1))
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin \\left(%s^\\circ \\right) \\cos \\left(%s^\\circ \\right)+%s\\sin \\left(%s^\\circ \\right) \\cos \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(a),latex(goc1),latex(goc2),latex(b),latex(goc3),latex(goc4))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq2))
                da_s1 = ' $%s$'%(latex(kq2+1))
                da_s2 = '$%s$'%(latex(kq2+2))
                da_s3 = '$%s$'%(latex(kq2-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq2))
                        )
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=\\sin \\left(%s^\\circ \\right) \\cos \\left(%s^\\circ \\right) \\sin \\left(%s^\\circ \\right) \\cos \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(goc1),latex(goc2),latex(goc3),latex(goc4))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq3))
                da_s1 = ' $%s$'%(latex(kq3+1))
                da_s2 = '$%s$'%(latex(kq3+2))
                da_s3 = '$%s$'%(latex(kq3-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq3))
                        )
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin^{2} \\left(%s^\\circ \\right)+%s\\cos^{2} \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(a),latex(goc1),latex(b),latex(goc2))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq4))
                da_s1 = ' $%s$'%(latex(kq4+1))
                da_s2 = '$%s$'%(latex(kq4+2))
                da_s3 = '$%s$'%(latex(kq4-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq4))
                        )
            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\tan \\left(%s^\\circ \\right)+%s\\cot \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(a),latex(goc5),latex(b),latex(goc6))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq5))
                da_s1 = ' $%s$'%(latex(kq5+1))
                da_s2 = '$%s$'%(latex(kq5+2))
                da_s3 = '$%s$'%(latex(kq5-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq5))
                        )
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Giá trị $P=%s\\sin^{2} \\left(%s^\\circ \\right)+%s\\cos^{2} \\left(%s^\\circ \\right)+%s\\tan^{2} \\left(%s^\\circ \\right)+%s\\cot^{2} \\left(%s^\\circ \\right)$ bằng \n'''
                            %(latex(a),latex(goc1),latex(b),latex(goc2),latex(c),latex(goc5),latex(d),latex(goc6))
                            )
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq6))
                da_s1 = ' $%s$'%(latex(kq6+1))
                da_s2 = '$%s$'%(latex(kq6+2))
                da_s3 = '$%s$'%(latex(kq6-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Sử dụng máy tính cầm tay ta tính được $P=%s$.'%(latex(kq6))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('=\\tilde{\\infty}','\\text{ là không xác định}').replace('\\tilde{\\infty}','\\text{Không xác định}')
            return content

