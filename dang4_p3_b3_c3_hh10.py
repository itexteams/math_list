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


def bt_dang4_p3_b3_c3_hh10(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                m=symbols('m')
                a1=randint(-9,9)
                b1=randint(-9,9)
                xm=randint(-9,9)
                ym=randint(-9,9)
                cm=randint(-9,9)
                a=2*a1
                b=2*b1
                c=-xm**2-ym**2-a*xm-b*ym

                while a**2+b**2-4*c<=0 or a1==0 or xm==0 or ym ==0:
                    x=symbols('x')
                    y=symbols('y')
                    m=symbols('m')
                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    xm=randint(-9,9)
                    ym=randint(-9,9)
                    cm=randint(-9,9)
                    a=2*a1
                    b=2*b1
                    c=-xm**2-ym**2-a*xm-b*ym


                dtr=a*x+b*y+c
                dthang=xm*x+ym*y+cm
                r=sqrt(a1**2+b1**2-c)
                dth1=dthang-cm


                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xm+a1), (ym+b1)), -(xm+a1)*xm-(ym+b1)*ym)
                # Rút gọn các hệ số
                hs_a = (xm+a1) // gcd
                hs_b = (ym+b1) // gcd
                hs_c = (-(xm+a1)*xm-(ym+b1)*ym) // gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dtt = hs_a*x+hs_b*y+hs_c
                kq=(xm*a1+ym*b1)+sqrt(xm**2+ym**2)*r+(xm*a1+ym*b1)-sqrt(xm**2+ym**2)*r



                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho đường tròn $(C): x^2+y^2+%s=0$ và đường thẳng $\\Delta:%s+m=0$. Biết rằng có hai giá trị $m_1$ và $m_2$ để $\\Delta$ tiếp xúc với $(C)$. Khi đó tổng $m_1+m_2$ bằng bao nhiêu?'
                                %(latex(dtr),latex(dth1)))
                # Nội dung lời giải
                loigiai = ('Đường tròn $(C)$ có tâm $I(%s;%s)$ và bán kính $R=\\sqrt{(%s)^2+(%s)^2-%s}=%s$.\\\\ \n'

                        '$\\Delta$ tiếp xúc với $(C)\\Leftrightarrow d(I,(\\Delta))=R \\Leftrightarrow \\dfrac{|%s\\cdot (%s)+%s\\cdot (%s)+m|}{\\sqrt{(%s)^2+(%s)^2}}=%s$'
                        '$$\\Leftrightarrow|%s+m|=%s\\Leftrightarrow \\heva{& m_1=%s \\\\ & m_2=%s}.$$'
                        'Vậy $m_1+m_2=\\left(%s\\right)+\\left(%s\\right)=%s$.'


                                %(latex(-a1),latex(-b1),latex(-a1),latex(-b1),latex(c),latex(r),

                                latex(xm),latex(-a1),latex(ym),latex(-b1),latex(xm),latex(ym),latex(r),
                                latex(-xm*a1-ym*b1),latex(sqrt(xm**2+ym**2)*r),latex((xm*a1+ym*b1)+sqrt(xm**2+ym**2)*r),latex((xm*a1+ym*b1)-sqrt(xm**2+ym**2)*r),
                                latex((xm*a1+ym*b1)+sqrt(xm**2+ym**2)*r),latex((xm*a1+ym*b1)-sqrt(xm**2+ym**2)*r),latex(kq),
                                )
                            )

                #Đáp án
                dapan='  \\shortans[0]{$%s$}   \n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\pm 0', '0').replace('1{x}', '{x}').replace('+0', '').replace('-0', '')
            return content 

