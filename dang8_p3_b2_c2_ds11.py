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


def bt_dang8_p3_b2_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis=[50000, 55000, 60000, 65000, 70000, 75000, 80000]
                u1=1
                lis1=[2000,3000,5000,1000]
                d=1
                n=randint(20,140)
                un=u1+(n-1)*d
                sn=n*u1+Rational(n*(n-1)*d,2)
                h1=sn

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chủ quán trà sữa muốn trang trí quán cho đẹp nên quyết định thuê thợ xây một bức tường bằng gạch (như hình vẽ). Biết hàng dưới cùng có $%s$ viên, mỗi hàng tiếp theo có ít hơn hàng trước $1$ viên và hàng trên cùng có đúng $1$ viên. \\\\ \n'
                                '\\begin{center}\n'
                                    '\\definecolor{ffqqqq}{rgb}{1.,0.,0.}\n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                        '\\clip(-0.686763379164798,-0.34345276182209467) rectangle (5.693611707281415,2.9560854721523246); \n'
                                        '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.12] (0.,0.) -- (0.,0.5) -- (0.5,0.5) -- (0.5,1.) -- (1.,1.) -- (1.,1.5) -- (1.5,1.5) -- (1.5,2.) -- (2.,2.) -- (2.,2.5) -- (3.,2.5) -- (3.,2.) -- (3.5,2.) -- (3.5,1.5) -- (4.,1.5) -- (4.,1.) -- (4.5,1.) -- (4.5,0.5) -- (5.,0.5) -- (5.,0.) -- cycle; \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.,0.)-- (0.,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.,0.5)-- (5.,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (5.,0.5)-- (5.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (5.,0.)-- (0.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.,0.5)-- (1.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.,0.5)-- (2.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.,0.5)-- (3.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.,0.5)-- (4.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.5,0.5)-- (0.5,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.5,1.)-- (4.5,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.5,1.)-- (4.5,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.5,1.)-- (1.5,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.5,1.)-- (2.5,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.5,1.)-- (3.5,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.,1.)-- (1.,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.,1.5)-- (4.,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.,1.5)-- (4.,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.,1.5)-- (2.,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.,1.5)-- (3.,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.5,1.5)-- (1.5,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.5,2.)-- (3.5,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.5,2.)-- (3.5,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.5,2.)-- (2.5,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.,2.)-- (2.,2.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.,2.5)-- (3.,2.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.,2.5)-- (3.,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.,0.)-- (0.,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.,0.5)-- (0.5,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.5,0.5)-- (0.5,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (0.5,1.)-- (1.,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.,1.)-- (1.,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.,1.5)-- (1.5,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.5,1.5)-- (1.5,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (1.5,2.)-- (2.,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.,2.)-- (2.,2.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (2.,2.5)-- (3.,2.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.,2.5)-- (3.,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.,2.)-- (3.5,2.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.5,2.)-- (3.5,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (3.5,1.5)-- (4.,1.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.,1.5)-- (4.,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.,1.)-- (4.5,1.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.5,1.)-- (4.5,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (4.5,0.5)-- (5.,0.5); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (5.,0.5)-- (5.,0.); \n'
                                        '\\draw [line width=1.pt,color=ffqqqq] (5.,0.)-- (0.,0.); \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Hỏi số gạch cần dùng để hoàn thành bức tường là bao nhiêu? \\\\ \n'
                                %(latex(un)
                                ))

                # Nội dung lời giải
                loigiai = ('Gọi $u_1, u_2, ..., u_n$ lần lượt là số gạch hàng trên cùng, hàng thứ hai,.... Các giá trị này lập thành một cấp số cộng với số hạng đầu $u_1=1$ và công sai $d=1$. \\\\ \n'
                        'Khi đó, tổng số gạch là \\\\ \n'
                        '\\hspace*{1cm} $S=\\dfrac{%s(%s-1)}{2}=%s$.\\\\ \n'
                        'Vậy số gạch cần dùng để hoàn thành bức tường là $%s$ viên.'

                        %(latex(un),latex(un),latex(sn),
                            latex(sn)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(sn))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0','')
            return content 

