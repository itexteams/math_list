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


def bt_dang11_p1_b1_c1_ds11(self):
            # Khai báo biến
            a=randint(1,89)
            a_rad=a * pi / 180
            b=randint(1,89)
            b_rad=b * pi / 180
            while b==a:
                a=randint(1,89)
                b=randint(1,89)
            m=randint(2,9)
            n=randint(2,9)
            while n==m:
                m=randint(2,9)
                n=randint(2,9)
            lis1=[30,45,60,120,135,150]
            goc1=random.choice(lis1)
            goc1_rad=goc1 * pi / 180
            a1=randint(1,30)
            a1_rad=a1 * pi / 180

            lis=['1','2','3','4','5','6','7','8'] 
            dang=random.choice(lis)

            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=%s\\sin^{2} %s+%s\\sin^{2} %s+%s\\sin^{2} %s+%s\\sin^{2} %s$ bằng \n'''
                            %(latex(m),latex(a_rad),latex(n),latex(b_rad),latex(m),latex(pi/2-a_rad),latex(n),latex(pi/2-b_rad)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(m+n))
                da_s1 = '$P=%s$'%(latex(m+n+1))
                da_s2 = '$P=%s$'%(latex(m+n-1))
                da_s3 = '$P=%s$'%(latex(m+n-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=%s\\sin^{2} %s +%s\\sin^{2} %s +%s\\sin^{2} %s +%s\\sin^{2} %s $ \\\\ \n'
                        '$P=%s\\left( \\sin^{2} %s +\\sin^{2} %s  \\right)+%s\\left(\\sin^{2} %s +\\sin^{2} %s  \\right)$ \\\\ \n'
                        '$P=%s\\left( \\sin^{2} %s +\\cos^{2} %s  \\right)+%s\\left(\\sin^{2} %s +\\cos^{2} %s  \\right)$ \\\\ \n'
                        '$P=%s \\cdot 1+%s \\cdot 1=%s$.'
                        %(latex(m),latex(a_rad),latex(n),latex(b_rad),latex(m),latex(pi/2-a_rad),latex(n),latex(pi/2-b_rad),
                        latex(m),latex(a_rad),latex(pi/2-a_rad),latex(n),latex(b_rad),latex(pi/2-b_rad),
                        latex(m),latex(a_rad),latex(a_rad),latex(n),latex(b_rad),latex(b_rad),
                        latex(m),latex(n),
                        latex(m+n)
                        )
                        )
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=\\tan %s  \\tan %s  \\tan %s  \\tan %s  \\tan %s $ bằng \n'''
                            %(latex(a_rad),latex(b_rad),latex(goc1_rad),latex(pi/2-a_rad),latex(pi/2-b_rad)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(tan(goc1_rad)))
                da_s1 = '$P=%s$'%(latex(tan(goc1_rad)-1))
                da_s2 = '$P=%s$'%(latex(tan(goc1_rad)+2))
                da_s3 = '$P=%s$'%(latex(tan(goc1_rad)+3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=\\tan %s  \\tan %s  \\tan %s  \\tan %s  \\tan %s $ \\\\ \n'
                        '$P=\\left( \\tan %s  \\tan %s  \\right)\\left(\\tan %s  \\tan %s  \\right) \\tan %s $ \\\\ \n'
                        '$P=\\left( \\tan %s  \\cot %s  \\right)\\left(\\tan %s  \\cot %s  \\right) \\tan %s $ \\\\ \n'
                        '$P=%s$.'
                        %(latex(a_rad),latex(b_rad),latex(goc1_rad),latex(pi/2-a_rad),latex(pi/2-b_rad),
                        latex(a_rad),latex(pi/2-a_rad),latex(b_rad),latex(pi/2-b_rad), latex(goc1_rad),
                        latex(a_rad),latex(a_rad),latex(b_rad),latex(b_rad), latex(goc1_rad),
                        latex(tan(goc1_rad))
                        )
                        )
            if dang=='7':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=\\cos %s  +\\cos %s  +\\cos %s  +\\cos %s +\\cos %s $ bằng \n'''
                            %(latex(a_rad),latex(b_rad),latex(pi-a_rad),latex(pi-b_rad),latex(goc1_rad)
                                ))

                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(cos(goc1_rad)))
                da_s1 = '$P=%s$'%(latex(cos(goc1_rad)+1))
                da_s2 = '$P=%s$'%(latex(cos(goc1_rad)-1))
                da_s3 = '$P=%s$'%(latex(cos(goc1_rad)+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=\\cos %s  +\\cos %s  +\\cos %s  +\\cos %s  +\\cos %s $ \\\\ \n'
                        '$P=\\left( \\cos %s  +\\cos %s  \\right)+\\left(\\cos %s  +\\cos %s  \\right) +\\cos %s $ \\\\ \n'
                        '$P=\\left( \\cos %s  -\\cos %s  \\right)+\\left(\\cos %s  -\\cos %s  \\right) +\\cos %s $ \\\\ \n'
                        '$P=%s$.'
                        %(latex(a_rad),latex(b_rad),latex(pi-a_rad),latex(pi-b_rad),latex(goc1_rad),
                        latex(a_rad),latex(pi-a_rad),latex(b_rad),latex(pi-b_rad), latex(goc1_rad),
                        latex(a_rad),latex(a_rad),latex(b_rad),latex(b_rad),latex(goc1_rad),
                        latex(cos(goc1_rad))
                        )
                        )
            if dang=='8':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=\\sin %s  \\cos %s  -\\sin %s  \\cos %s $ bằng \n'''
                            %(latex(goc1_rad+a1_rad),latex(a1_rad),latex(pi/2+goc1_rad+a1_rad),latex(pi/2-a1_rad)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(sin(goc1_rad)))
                da_s1 = '$P=%s$'%(latex(sin(goc1_rad)+1))
                da_s2 = '$P=%s$'%(latex(sin(goc1_rad)-1))
                da_s3 = '$P=%s$'%(latex(sin(goc1_rad)+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=\\sin %s  \\cos %s  -\\sin %s  \\cos %s $ \\\\ \n'
                        '$P=\\sin %s  \\cos %s  -\\sin \\left( \\dfrac{\\pi}{2}  +%s \\right) \\cos \\left( \\dfrac{\\pi}{2} -%s \\right)$ \\\\ \n'
                        '$P=\\sin %s  \\cos %s  -\\cos %s  \\sin %s $ \\\\ \n'
                        '$P=\\sin \\left( %s -%s \\right)$\\\\ \n'
                        '$P=\\sin %s $ \\\\ \n'
                        '$P=%s$.'
                        %(latex(goc1_rad+a1_rad),latex(a1_rad),latex(pi/2+goc1_rad+a1_rad),latex(pi/2-a1_rad),
                        latex(goc1_rad+a1_rad),latex(a1_rad),latex(goc1_rad+a1_rad),latex(a1_rad),
                        latex(goc1_rad+a1_rad),latex(a1_rad),latex(goc1_rad+a1_rad),latex(a1_rad),
                        latex(goc1_rad+a1_rad),latex(a1_rad),
                        latex(goc1_rad),
                        latex(sin(goc1_rad))
                        )
                        )

            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=%s\\sin^{2} %s^\\circ+%s\\sin^{2} %s^\\circ+%s\\sin^{2} %s^\\circ+%s\\sin^{2} %s^\\circ$ bằng \n'''
                            %(latex(m),latex(a),latex(n),latex(b),latex(m),latex(90-a),latex(n),latex(90-b)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(m+n))
                da_s1 = '$P=%s$'%(latex(m+n+1))
                da_s2 = '$P=%s$'%(latex(m+n-1))
                da_s3 = '$P=%s$'%(latex(m+n-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=%s\\sin^{2} %s^\\circ+%s\\sin^{2} %s^\\circ+%s\\sin^{2} %s^\\circ+%s\\sin^{2} %s^\\circ$ \\\\ \n'
                        '$P=%s\\left( \\sin^{2} %s^\\circ+\\sin^{2} %s^\\circ \\right)+%s\\left(\\sin^{2} %s^\\circ+\\sin^{2} %s^\\circ \\right)$ \\\\ \n'
                        '$P=%s\\left( \\sin^{2} %s^\\circ+\\cos^{2} %s^\\circ \\right)+%s\\left(\\sin^{2} %s^\\circ+\\cos^{2} %s^\\circ \\right)$ \\\\ \n'
                        '$P=%s \\cdot 1+%s \\cdot 1=%s$.'
                        %(latex(m),latex(a),latex(n),latex(b),latex(m),latex(90-a),latex(n),latex(90-b),
                        latex(m),latex(a),latex(90-a),latex(n),latex(b),latex(90-b),
                        latex(m),latex(a),latex(a),latex(n),latex(b),latex(b),
                        latex(m),latex(n),
                        latex(m+n)
                        )
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=\\tan %s^\\circ \\tan %s^\\circ \\tan %s^\\circ \\tan %s^\\circ \\tan %s^\\circ$ bằng \n'''
                            %(latex(a),latex(b),latex(goc1),latex(90-a),latex(90-b)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(tan(goc1_rad)))
                da_s1 = '$P=%s$'%(latex(tan(goc1_rad)-1))
                da_s2 = '$P=%s$'%(latex(tan(goc1_rad)+2))
                da_s3 = '$P=%s$'%(latex(tan(goc1_rad)+3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=\\tan %s^\\circ \\tan %s^\\circ \\tan %s^\\circ \\tan %s^\\circ \\tan %s^\\circ$ \\\\ \n'
                        '$P=\\left( \\tan %s^\\circ \\tan %s^\\circ \\right)\\left(\\tan %s^\\circ \\tan %s^\\circ \\right) \\tan %s^\\circ$ \\\\ \n'
                        '$P=\\left( \\tan %s^\\circ \\cot %s^\\circ \\right)\\left(\\tan %s^\\circ \\cot %s^\\circ \\right) \\tan %s^\\circ$ \\\\ \n'
                        '$P=%s$.'
                        %(latex(a),latex(b),latex(goc1),latex(90-a),latex(90-b),
                        latex(a),latex(90-a),latex(b),latex(90-b), latex(goc1),
                        latex(a),latex(a),latex(b),latex(b), latex(goc1),
                        latex(tan(goc1_rad))
                        )
                        )
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=\\cos %s^\\circ +\\cos %s^\\circ +\\cos %s^\\circ +\\cos %s^\\circ+\\cos %s^\\circ$ bằng \n'''
                            %(latex(a),latex(b),latex(180-a),latex(180-b),latex(goc1)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(cos(goc1_rad)))
                da_s1 = '$P=%s$'%(latex(cos(goc1_rad)+1))
                da_s2 = '$P=%s$'%(latex(cos(goc1_rad)-1))
                da_s3 = '$P=%s$'%(latex(cos(goc1_rad)+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=\\cos %s^\\circ +\\cos %s^\\circ +\\cos %s^\\circ +\\cos %s^\\circ +\\cos %s^\\circ$ \\\\ \n'
                        '$P=\\left( \\cos %s^\\circ +\\cos %s^\\circ \\right)+\\left(\\cos %s^\\circ +\\cos %s^\\circ \\right) +\\cos %s^\\circ$ \\\\ \n'
                        '$P=\\left( \\cos %s^\\circ -\\cos %s^\\circ \\right)+\\left(\\cos %s^\\circ -\\cos %s^\\circ \\right) +\\cos %s^\\circ$ \\\\ \n'
                        '$P=%s$.'
                        %(latex(a),latex(b),latex(180-a),latex(180-b),latex(goc1),
                        latex(a),latex(180-a),latex(b),latex(180-b), latex(goc1),
                        latex(a),latex(a),latex(b),latex(b),latex(goc1),
                        latex(cos(goc1_rad))
                        )
                        )
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Giá trị của biểu thức $P=\\sin %s^\\circ \\cos %s^\\circ -\\sin %s^\\circ \\cos %s^\\circ$ bằng \n'''
                            %(latex(goc1+a1),latex(a1),latex(90+goc1+a1),latex(90-a1)
                                )
                            )
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(sin(goc1_rad)))
                da_s1 = '$P=%s$'%(latex(sin(goc1_rad)+1))
                da_s2 = '$P=%s$'%(latex(sin(goc1_rad)-1))
                da_s3 = '$P=%s$'%(latex(sin(goc1_rad)+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=\\sin %s^\\circ \\cos %s^\\circ -\\sin %s^\\circ \\cos %s^\\circ$ \\\\ \n'
                        '$P=\\sin %s^\\circ \\cos %s^\\circ -\\sin (90^\\circ +%s^\\circ) \\cos (90^\\circ-%s^\\circ)$ \\\\ \n'
                        '$P=\\sin %s^\\circ \\cos %s^\\circ -\\cos %s^\\circ \\sin %s^\\circ$ \\\\ \n'
                        '$P=\\sin (%s^\\circ-%s^\\circ)$\\\\ \n'
                        '$P=\\sin %s^\\circ$ \\\\ \n'
                        '$P=%s$.'
                        %(latex(goc1+a1),latex(a1),latex(90+goc1+a1),latex(90-a1),
                        latex(goc1+a1),latex(a1),latex(goc1+a1),latex(a1),
                        latex(goc1+a1),latex(a1),latex(goc1+a1),latex(a1),
                        latex(goc1+a1),latex(a1),
                        latex(goc1),
                        latex(sin(goc1_rad))
                        )
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-')
            return content

