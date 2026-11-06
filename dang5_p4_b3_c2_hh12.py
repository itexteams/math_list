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


def bt_dang5_p4_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x0=randint(-9,9)
                y0=randint(-9,9)
                z0=randint(-9,9)

                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)

                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)

                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)

                xc=randint(-9,9)
                yc=randint(-9,9)
                zc=randint(-9,9)

                xd=randint(-9,9)
                yd=randint(-9,9)
                zd=randint(-9,9)

                x1=xb-xa
                y1=yb-ya
                z1=zb-za

                x2=xd-xc
                y2=yd-yc
                z2=zd-zc
                while xa==0 or xb==0 or xa==0 or xd==0 or x1*y2==x2*y1:
                    x=symbols('x')
                    y=symbols('y')
                    z=symbols('z')

                    x0=randint(-9,9)
                    y0=randint(-9,9)
                    z0=randint(-9,9)

                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)

                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    za=randint(-9,9)

                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    zb=randint(-9,9)

                    xc=randint(-9,9)
                    yc=randint(-9,9)
                    zc=randint(-9,9)

                    xd=randint(-9,9)
                    yd=randint(-9,9)
                    zd=randint(-9,9)

                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za

                    x2=xd-xc
                    y2=yd-yc
                    z2=zd-zc


                daiu=sqrt(x1**2+y1**2+z1**2)
                dain=sqrt(x2**2+y2**2+z2**2)
                tu=abs(x1*x2+y1*y2+z1*z2)
                mau=daiu*dain

                gtsin=tu/mau

                g=math.degrees(math.acos(gtsin))
                kq1=g
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


                # Câu hỏi
                noidungcauhoi = ('Trong không gian với hệ tọa độ $Oxyz$, Cho bốn điểm $A(%s;%s;%s),B(%s;%s;%s),$\\\\ \n'
                                '$C(%s;%s;%s),D(%s;%s;%s)$. Tính góc giữa đường thẳng $AB$ và $CD$.'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb), latex(xc),latex(yc),latex(zc),latex(xd),latex(yd),latex(zd))
                                )

                # Nội dung lời giải
                loigiai = ('Đường thẳng $AB$ có một vectơ chỉ phương là $\\vec{AB}=(%s;%s;%s)$.\\\\ \n'
                        'Đường thẳng $CD$ có một vectơ chỉ phương là $\\vec{CD}=(%s;%s;%s)$.\\\\ \n'
                        'Gọi $\\varphi$ là góc tạo bởi hai đường thẳng $AB$ và $CD$. \\\\ \n'
                        'Ta có $$\\cos\\varphi=\\left|\\cos(\\vec{AB},\\vec{CD})\\right|=\\dfrac{|%s\\cdot (%s)+%s\\cdot (%s)+%s\\cdot (%s)|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot \\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$$'
                        '$\\Rightarrow \\varphi \\approx %s^0$.'


                        %(latex(x1),latex(y1),latex(z1),
                            latex(x2),latex(y2),latex(z2),

                            latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2), latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(gtsin),latex(kq),
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content   

