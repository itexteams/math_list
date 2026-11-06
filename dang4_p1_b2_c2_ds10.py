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


def bt_dang4_p1_b2_c2_ds10(self):
            #Khai báo biến

            x = symbols('x')
            y = symbols('y')
            lis1=[-4,-3,-2,-1]
            lis2=[1,2,3,4]
            a=random.choice(lis1)
            b=random.choice(lis2)
            #phương trình
            pt=b*x+a*y-a*b
            #cắt đường x=-5,x=5
            y1=b+5*b/a
            y2=b-5*b/a
            lis3=[1,2,3,4]
            lis4=[1,2,3,4]
            a1=random.choice(lis3)
            b1=random.choice(lis4)
            #phương trình
            pt1=b1*x+a1*y-a1*b1
            #cắt đường x=-5,x=5
            y11=b1+5*b1/a1
            y21=b1-5*b1/a1

            pt2=b*x+a1*y-a1*b
            pt3=b1*x+a*y-a*b1

            lis=['1','2','3','4','5','6']
            dang=random.choice(lis)

            #Nội dung câu hỏi
            noidungcauhoi = ('''Hình vẽ bên biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn nào dưới đây? '''
                                )
            if dang=='1':      
                # Các đáp án
                da_d = '\\True $\\heva{&%s \\ge 0\\\\&%s \\le 0}$' %(latex(pt),latex(pt1)) 
                da_s1 = '$\\heva{&%s \\le 0\\\\&%s \\ge 0}$' %(latex(pt),latex(pt1))   
                da_s2 = '$\\heva{&%s \\ge 0\\\\&%s \\le 0}$' %(latex(pt2),latex(pt3))  
                da_s3 = '$\\heva{&%s \\le 0\\\\&%s \\ge 0}$' %(latex(pt2),latex(pt3)) 
                hinhve=(
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] \n'
                                '\\draw[->] (-5,0)--(5,0) node[below]{$x$}; \n'
                                '\\draw[->] (0,-5)--(0,5) node[left]{$y$}; \n'
                                '\\draw (0,0) node[below left]{$O$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\draw[blue] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\draw[red] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\fill[pattern=north east lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\fill[pattern=north west lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\foreach \\x in {%s,%s} \n'
                                '\\draw (\\x,2pt) -- (\\x,-2pt) node [below] {$\\x$}; \n'
                                '\\foreach \\y in {%s,%s} \n'
                                '\\draw (2pt,\\y) -- (-2pt,\\y) node [left] {$\\y$}; \n'
                            '\\end{tikzpicture} \n'
                            %(latex(y1),latex(y2),latex(y11),latex(y21),latex(y1),latex(y2),latex(y11),latex(y21),latex(a),latex(a1),latex(b),latex(b1)
                            ))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta thấy \\\\'
                        'Hai đường thẳng $d_1:%s=0$ và $d_2:%s=0$ có đồ thị như hình vẽ. \\\\'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s \\ge 0$. \\\\ \n'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s \\le 0$. \\\\ \n'
                            'Nên biểu diễn miền nghiệm của bất phương trình là nửa mặt phẳng (không bị gạch chéo) tính cả hai đường thẳng.'
                            %(latex(pt),latex(pt1),latex(pt),latex(pt1)) 
                                )
            if dang=='2':      
                # Các đáp án
                da_d = '\\True $\\heva{&%s > 0\\\\&%s < 0}$' %(latex(pt),latex(pt1)) 
                da_s1 = '$\\heva{&%s < 0\\\\&%s > 0}$' %(latex(pt),latex(pt1))   
                da_s2 = '$\\heva{&%s \\le 0\\\\&%s \\ge 0}$' %(latex(pt2),latex(pt3))  
                da_s3 = '$\\heva{&%s < 0\\\\&%s > 0}$' %(latex(pt2),latex(pt3)) 
                hinhve=(
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] \n'
                                '\\draw[->] (-5,0)--(5,0) node[below]{$x$}; \n'
                                '\\draw[->] (0,-5)--(0,5) node[left]{$y$}; \n'
                                '\\draw (0,0) node[below left]{$O$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\draw[dashed,blue] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\draw[dashed,red] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\fill[pattern=north east lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\fill[pattern=north west lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\foreach \\x in {%s,%s} \n'
                                '\\draw (\\x,2pt) -- (\\x,-2pt) node [below] {$\\x$}; \n'
                                '\\foreach \\y in {%s,%s} \n'
                                '\\draw (2pt,\\y) -- (-2pt,\\y) node [left] {$\\y$}; \n'
                            '\\end{tikzpicture} \n'
                            %(latex(y1),latex(y2),latex(y11),latex(y21),latex(y1),latex(y2),latex(y11),latex(y21),latex(a),latex(a1),latex(b),latex(b1)
                            ))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta thấy \\\\'
                        'Hai đường thẳng $d_1:%s=0$ và $d_2:%s=0$ có đồ thị như hình vẽ. \\\\'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s > 0$. \\\\ \n'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s < 0$. \\\\ \n'
                            'Nên biểu diễn miền nghiệm của bất phương trình là nửa mặt phẳng (không bị gạch chéo) không tính hai đường thẳng.'
                            %(latex(pt),latex(pt1),latex(pt),latex(pt1)) 
                                )
            if dang=='3':      
                # Các đáp án
                da_d = '\\True $\\heva{&%s \\le 0\\\\&%s \\le 0}$' %(latex(pt),latex(pt1)) 
                da_s1 = '$\\heva{&%s \\ge 0\\\\&%s \\ge 0}$' %(latex(pt),latex(pt1))   
                da_s2 = '$\\heva{&%s > 0\\\\&%s < 0}$' %(latex(pt2),latex(pt3))  
                da_s3 = '$\\heva{&%s \\le 0\\\\&%s \\ge 0}$' %(latex(pt2),latex(pt3)) 
                hinhve=(
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] \n'
                                '\\draw[->] (-5,0)--(5,0) node[below]{$x$}; \n'
                                '\\draw[->] (0,-5)--(0,5) node[left]{$y$}; \n'
                                '\\draw (0,0) node[below left]{$O$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\draw[blue] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\draw[red] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\fill[pattern=north east lines, pattern color=black, opacity=0.9] (-5,-5) -- (5,-5) -- (5,%s) -- (-5,%s) -- cycle; \n'	
                                '\\fill[pattern=north west lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\foreach \\x in {%s,%s} \n'
                                '\\draw (\\x,2pt) -- (\\x,-2pt) node [below] {$\\x$}; \n'
                                '\\foreach \\y in {%s,%s} \n'
                                '\\draw (2pt,\\y) -- (-2pt,\\y) node [left] {$\\y$}; \n'
                            '\\end{tikzpicture} \n'
                            %(latex(y1),latex(y2),latex(y11),latex(y21),latex(y2),latex(y1),latex(y11),latex(y21),latex(a),latex(a1),latex(b),latex(b1)
                            ))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta thấy \\\\'
                        'Hai đường thẳng $d_1:%s=0$ và $d_2:%s=0$ có đồ thị như hình vẽ. \\\\'
                        'Tọa độ điểm $O(0;0)$ không thỏa mãn bất phương trình $%s \\le 0$. \\\\ \n'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s \\le 0$. \\\\ \n'
                            'Nên biểu diễn miền nghiệm của bất phương trình là nửa mặt phẳng (không bị gạch chéo) tính cả hai đường thẳng.'
                            %(latex(pt),latex(pt1),latex(pt),latex(pt1)) 
                                )
            if dang=='4':      
                # Các đáp án
                da_d = '\\True $\\heva{&%s < 0\\\\&%s > 0}$' %(latex(pt),latex(pt1)) 
                da_s1 = '$\\heva{&%s < 0\\\\&%s \\le 0}$' %(latex(pt),latex(pt1))   
                da_s2 = '$\\heva{&%s \\ 0\\\\&%s < 0}$' %(latex(pt2),latex(pt3))  
                da_s3 = '$\\heva{&%s < 0\\\\&%s \\ge 0}$' %(latex(pt2),latex(pt3)) 
                hinhve=(
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] \n'
                                '\\draw[->] (-5,0)--(5,0) node[below]{$x$}; \n'
                                '\\draw[->] (0,-5)--(0,5) node[left]{$y$}; \n'
                                '\\draw (0,0) node[below left]{$O$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\draw[dashed,blue] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\draw[dashed,red] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\fill[pattern=north east lines, pattern color=black, opacity=0.9] (-5,-5) -- (5,-5) -- (5,%s) -- (-5,%s) -- cycle; \n'	
                                '\\fill[pattern=north west lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\foreach \\x in {%s,%s} \n'
                                '\\draw (\\x,2pt) -- (\\x,-2pt) node [below] {$\\x$}; \n'
                                '\\foreach \\y in {%s,%s} \n'
                                '\\draw (2pt,\\y) -- (-2pt,\\y) node [left] {$\\y$}; \n'
                            '\\end{tikzpicture} \n'
                            %(latex(y1),latex(y2),latex(y11),latex(y21),latex(y2),latex(y1),latex(y11),latex(y21),latex(a),latex(a1),latex(b),latex(b1)
                            ))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta thấy \\\\'
                        'Hai đường thẳng $d_1:%s=0$ và $d_2:%s=0$ có đồ thị như hình vẽ. \\\\'
                        'Tọa độ điểm $O(0;0)$ không thỏa mãn bất phương trình $%s < 0$. \\\\ \n'
                        'Tọa độ điểm $O(0;0)$ không thỏa mãn bất phương trình $%s > 0$. \\\\ \n'
                            'Nên biểu diễn miền nghiệm của bất phương trình là nửa mặt phẳng (không bị gạch chéo) không tính hai đường thẳng.'
                            %(latex(pt),latex(pt1),latex(pt),latex(pt1)) 
                                )
            if dang=='5':      
                # Các đáp án
                da_d = '\\True $\\heva{&%s \\ge 0\\\\&%s \\ge 0}$' %(latex(pt),latex(pt1)) 
                da_s1 = '$\\heva{&%s > 0\\\\&%s < 0}$' %(latex(pt),latex(pt1))   
                da_s2 = '$\\heva{&%s \\ge 0\\\\&%s \\le 0}$' %(latex(pt2),latex(pt3))  
                da_s3 = '$\\heva{&%s < 0\\\\&%s \\le 0}$' %(latex(pt2),latex(pt3)) 
                hinhve=(
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] \n'
                                '\\draw[->] (-5,0)--(5,0) node[below]{$x$}; \n'
                                '\\draw[->] (0,-5)--(0,5) node[left]{$y$}; \n'
                                '\\draw (0,0) node[below left]{$O$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\draw[blue] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\draw[red] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\fill[pattern=north east lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\fill[pattern=north west lines, pattern color=black, opacity=0.9] (-5,-5) -- (5,-5) -- (5,%s) -- (-5,%s) -- cycle; \n'
                                '\\foreach \\x in {%s,%s} \n'
                                '\\draw (\\x,2pt) -- (\\x,-2pt) node [below] {$\\x$}; \n'
                                '\\foreach \\y in {%s,%s} \n'
                                '\\draw (2pt,\\y) -- (-2pt,\\y) node [left] {$\\y$}; \n'
                            '\\end{tikzpicture} \n'
                            %(latex(y1),latex(y2),latex(y11),latex(y21),latex(y1),latex(y2),latex(y21),latex(y11),latex(a),latex(a1),latex(b),latex(b1)
                            ))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta thấy \\\\'
                        'Hai đường thẳng $d_1:%s=0$ và $d_2:%s=0$ có đồ thị như hình vẽ. \\\\'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s \\ge 0$. \\\\ \n'
                        'Tọa độ điểm $O(0;0)$ không thỏa mãn bất phương trình $%s \\ge 0$. \\\\ \n'
                            'Nên biểu diễn miền nghiệm của bất phương trình là nửa mặt phẳng (không bị gạch chéo) tính cả hai đường thẳng.'
                            %(latex(pt),latex(pt1),latex(pt),latex(pt1)) 
                                )
            if dang=='6':      
                # Các đáp án
                da_d = '\\True $\\heva{&%s > 0\\\\&%s > 0}$' %(latex(pt),latex(pt1)) 
                da_s1 = '$\\heva{&%s \\ge 0\\\\&%s \\le 0}$' %(latex(pt),latex(pt1))   
                da_s2 = '$\\heva{&%s > 0\\\\&%s < 0}$' %(latex(pt2),latex(pt3))  
                da_s3 = '$\\heva{&%s \\le 0\\\\&%s \\ge 0}$' %(latex(pt2),latex(pt3)) 
                hinhve=(
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] \n'
                                '\\draw[->] (-5,0)--(5,0) node[below]{$x$}; \n'
                                '\\draw[->] (0,-5)--(0,5) node[left]{$y$}; \n'
                                '\\draw (0,0) node[below left]{$O$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\draw[dashed,blue] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\draw[dashed,red] (-5,%s) -- (5,%s) node[right] {$d$}; \n'
                                '\\clip (-5,-5) rectangle (5,5); \n'
                                '\\fill[pattern=north east lines, pattern color=black, opacity=0.9] (-5,%s) -- (5,%s) -- (5,5) -- (-5,5) -- cycle; \n'	
                                '\\fill[pattern=north west lines, pattern color=black, opacity=0.9] (-5,-5) -- (5,-5) -- (5,%s) -- (-5,%s) -- cycle; \n'
                                '\\foreach \\x in {%s,%s} \n'
                                '\\draw (\\x,2pt) -- (\\x,-2pt) node [below] {$\\x$}; \n'
                                '\\foreach \\y in {%s,%s} \n'
                                '\\draw (2pt,\\y) -- (-2pt,\\y) node [left] {$\\y$}; \n'
                            '\\end{tikzpicture} \n'
                            %(latex(y1),latex(y2),latex(y11),latex(y21),latex(y1),latex(y2),latex(y21),latex(y11),latex(a),latex(a1),latex(b),latex(b1)
                            ))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta thấy \\\\'
                        'Hai đường thẳng $d_1:%s=0$ và $d_2:%s=0$ có đồ thị như hình vẽ. \\\\'
                        'Tọa độ điểm $O(0;0)$ thỏa mãn bất phương trình $%s > 0$. \\\\ \n'
                        'Tọa độ điểm $O(0;0)$ không thỏa mãn bất phương trình $%s > 0$. \\\\ \n'
                            'Nên biểu diễn miền nghiệm của bất phương trình là nửa mặt phẳng (không bị gạch chéo) tính cả hai đường thẳng.'
                            %(latex(pt),latex(pt1),latex(pt),latex(pt1)) 
                                )
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\immini{'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n}{'+hinhve+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('++','+').replace('+-','-')
            return content

