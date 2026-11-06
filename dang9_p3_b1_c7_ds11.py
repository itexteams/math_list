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


def bt_dang9_p3_b1_c7_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x0=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                a=randint(1,5)
                b=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                c=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                d=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                while a*d-b*c==0 or -d/c==x0:
                    x0=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                    a=randint(1,5)
                    b=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                    c=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
                    d=random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])

                x=symbols('x')
                y=(a*x+b)/(c*x+d)
                y0=Rational(a*x0+b,c*x0+d)

                dh=(a-c*y0)/(c*x+d)

                dh0=Rational(a-c*y0,c*x0+d)

                h1=dh0-dh0*x0+y0   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)=%s$. Phương trình tiếp tuyến của đồ thị hàm số tại điểm $\\left(%s;%s\\right)$ có dạng $y=ax+b$. Tổng $a + b$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                %(latex(y),latex(x0),latex(y0)
                                ))

                # Nội dung lời giải
                loigiai=('''Tiếp tuyến có hệ số góc là \\\\
                        $f'(%s)=\\underset{x\\to %s}{\\mathop{\\lim }} \\frac{f(x)-f(%s)}{x-%s}=\\underset{x\\to %s}{\\mathop{\\lim }} \\frac{%s}{x-%s}$ \\\\
                            $f'(%s)=\\underset{x\\to %s}{\\mathop{\\lim }} \\frac{%s}{(%s)(%s)}=\\underset{x\\to %s}{\\mathop{\\lim }} \\left[ %s \\right]=%s$.\\\\
                                Phương trình tiếp tuyến là \\\\
                                    $y=%s(%s)+%s \\Leftrightarrow y=%s$.\\\\
                                        Suy ra $a=%s; b=%s$ và $a+b=%s \\approx %s$.'''
                        %(latex(x0),latex(x0),latex(x0),latex(x0),
                        latex(x0),latex(y-y0),latex(x0),
                        latex(x0),latex(x0),latex((a-c*y0)*x+b-y0*d),latex(c*x+d),latex(x-x0),
                        latex(x0),latex(dh),latex(dh0),
                        latex(dh0),latex(x-x0),latex(y0),latex(dh0*x-dh0*x0+y0),
                        latex(dh0),latex(-dh0*x0+y0),latex(dh0-dh0*x0+y0),latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--', '+')
            return content           

