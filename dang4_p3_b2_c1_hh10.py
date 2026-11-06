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


def bt_dang4_p3_b2_c1_hh10(self):
            # Khai báo biến
            lis0=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]
            goc=random.choice(lis0)
            goc_rad=goc * pi / 180

            goc1=180-goc
            goc1_rad=goc1 * pi / 180

            goc2=180-(90-goc)
            goc2_rad=goc2 * pi / 180

            goc3=90-goc
            goc3_rad=goc3 * pi / 180

            lis1=[50,55,60,65,70,75,80,85,90,95]
            a=random.choice(lis1)

            b=randint(5,11)
            lis3=[1,1.5,2,2.5,3,3.5,4,4.5]
            t1=random.choice(lis3)
            t2=random.choice(lis3)

            lis4=[-1,-2,-3,1,2,3]
            i1=random.choice(lis4)
            lis4.remove(i1)
            i2=random.choice(lis4)
            lis4.remove(i2)
            i3=random.choice(lis4)

            kq1=round(sqrt((a*t1)**2+(b*t2)**2-2*a*t1*b*t2*cos(goc1_rad)),1)
            kq2=round(sqrt((a*t1)**2+(b*t2)**2-2*a*t1*b*t2*cos(goc2_rad)),1)
            kq3=round(sqrt((a*t1)**2+(b*t2)**2-2*a*t1*b*t2*cos(goc3_rad)),1)
            kq4=round(sqrt((a*t1)**2+(b*t2)**2-2*a*t1*b*t2*cos(goc_rad)),1)

            number = Decimal(float(kq1))  # Số cần làm tròn
            kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            lis=['1']
            dang=random.choice(lis)
            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một tàu đánh cá xuất phát từ cảng $A$ đi theo hướng $S %s^\\circ E$ với vận tốc $%s$ km/h, đi được $%s$ giờ thì động cơ của tàu bị hỏng nên tàu trôi tự do theo hướng nam với vận tốc $%s$ km/h$zzz$ Sau $%s$ giờ kể từ khi động cơ bị hỏng, tàu neo đậu được vào một hòn đảo$zzz$ Khoảng cách từ cảng $A$ đến hòn đào nơi tàu neo đậu là bao nhiêu km? (kết quả làm tròn đến hàng đơn vị)$zzz$  \n'''
                            %(latex(goc),latex(a),latex(t1), latex(b), latex(t2)
                            ))

                # Nội dung lời giải
                loigiai = ('Khoảng cách từ cảng $A$ đến điểm tàu chết máy là \\\\ \n'
                        '\\hspace*{1cm} $AB=%s \\cdot %s =%s$ km$zzz$\\\\ \n'
                        'Khoảng cách từ điểm tàu chết máy đến vị trí neo đậu là \\\\ \n'
                        '\\hspace*{1cm} $BC=%s \\cdot %s =%s$ km$zzz$\\\\ \n'
                        'Theo giả thiết tàu đi theo hướng $S %s^\\circ E$ nên $\\widehat{SAB} =%s^\\circ$ và $\\widehat{ABC} =180^\\circ-%s^\\circ =%s^\\circ$$zzz$ \\\\ \n'
                        'Khoảng cách từ cảng $A$ đến vị trí tàu neo đậu là $AC$$zzz$ \\\\ \n'
                        'Áp dụng định lí cosin ta có \\\\ \n'
                        '\\hspace*{1cm} $AC=\\sqrt{AB^2+BC^2-2AB \\cdot BC \\cdot \\cos B}$\\\\ \n'
                        '\\hspace*{1cm} $AC=\\sqrt{%s^2+%s^2-2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ} \\approx %s$ km$zzz$'
                        %(latex(a), latex(t1), latex(a*t1), #AB
                        latex(b), latex(t2), latex(b*t2), #AC
                        latex(goc),latex(goc),latex(goc),latex(goc1),
                        latex(a*t1),latex(b*t2),latex(a*t1),latex(b*t2),latex(goc1),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zzz$', '.')     
            return content 

