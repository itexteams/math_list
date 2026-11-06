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


def bt_dang1_p3_b2_c1_hh10(self):
            # Khai báo biến
            lis0=[30,45,60,90,120,135,150]
            goc=random.choice(lis0)
            goc_rad=goc * pi / 180
            lis1=[15,20,25,30,35,40,45,50,55,60]
            a=random.choice(lis1)
            b=random.choice(lis1)
            lis3=[1,1.5,2,2.5,3,3.5,4,4.5]
            t=random.choice(lis3)

            kq1=sqrt((a*t)**2+(b*t)**2-2*a*t*b*t*cos(goc_rad))
            number = Decimal(float(kq1))  # Số cần làm tròn
            kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Nội dung câu hỏi
                noidungcauhoi = ('''Hai chiếc tàu thủy cùng xuất phát từ vị trí $A$ đi thẳng theo hai hướng tạo với nhau một góc $%s^\\circ$$zzz$ Tàu thứ nhất chạy với tốc độ $%s$ km/h, tàu thứ hai chạy với tốc độ $%s$ km/h$zzz$ Sau $%s$ giờ khoảng cách giữa hai tàu là bao nhiêu km? (kết quả làm tròn đến hàng đơn vị)$zzz$  \n'''
                            %(latex(goc),latex(a),latex(b),latex(t)
                            ))

                # Nội dung lời giải
                loigiai = ('Sau $%s$ giờ: \\\\ \n'
                        'Quãng đường tàu thứ nhất đi được là $S_1=%s \\cdot %s = %s$ km$zzz$ \\\\ \n '
                        'Quãng đường tàu thứ hai đi được là $S_2=%s \\cdot %s = %s$ km$zzz$ \\\\ \n '
                        'Sau $%s$ giờ, khoảng cách giữa hai tàu là \\\\ \n'
                        '$S=\\sqrt{S_1^2+S_2^2-2 S_1 \\cdot S_2 \\cdot \\cos %s^\\circ} = \\sqrt{%s^2+%s^2-2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ}\\approx %s$ km$zzz$'
                        %(latex(t),
                        latex(a), latex(t), latex(a*t),
                        latex(b), latex(t), latex(b*t),  
                        latex(t),latex(goc),
                        latex(a*t),latex(b*t),latex(a*t),latex(b*t), latex(goc), latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zzz$', '.').replace(',0', '')
            return content

