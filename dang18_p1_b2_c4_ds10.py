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


def bt_dang18_p1_b2_c4_ds10(self):
            #Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(3,6)
                a=randint(20,30)
                b=a+k
                lis1=[400,450,500,550,600,650]
                c=random.choice(lis1)
                d=1
                lis2=[100,150,200,250]
                e=random.choice(lis2)
                f=expand((k-x)*(c+e*x), x)
                x0=Rational(k*e-c,2*e)
                f0=(k-x0)*(c+e*x0)
                kq=b-x0
                xkq=float(x0)
                while xkq<=0:
                    x=symbols('x')
                    k=randint(3,6)
                    a=randint(20,30)
                    b=a+k
                    lis1=[400,450,500,550,600,650]
                    c=random.choice(lis1)
                    d=1
                    lis2=[100,150,200,250]
                    e=random.choice(lis2)
                    f=expand((k-x)*(c+e*x), x)
                    x0=Rational(k*e-c,2*e)
                    f0=(k-x0)*(c+e*x0)
                    kq=b-x0
                    xkq=float(x0)                       
                h1=kq   
                number = Decimal(float(h1))  # Số cần làm tròn
                ykq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(ykq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ykq+1)),
                    '$%s$'%(latex(ykq+2)),
                    '$%s$'%(latex(ykq+3)),
                    '$%s$'%(latex(ykq-1)),
                    '$%s$'%(latex(ykq-2)),
                    '$%s$'%(latex(ykq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Một doanh nghiệp tư nhân chuyên kinh doanh xe gắn máy các loại. Hiện nay doanh nghiệp đang tập trung chiến lược vào kinh doanh xe máy nhãn hiệu A với chi phí mua vào một chiếc là $%s$ triệu đồng và bán ra với giá là $%s$ triệu đồng. Với giá bán này thì số lượng xe mà khách hàng sẽ mua trong một năm là $%s$ chiếc. Nhằm mục tiêu đẩy mạnh hơn nữa lượng tiêu thụ dòng xe đang ăn khách này, doanh nghiệp dự định giảm giá bán và ước tính rằng nếu giảm $%s$ triệu đồng mỗi chiếc xe thì số lượng xe bán ra trong một năm là sẽ tăng thêm $%s$ chiếc. Giá bán mới để sau khi đã thực hiện giảm giá để thu được lợi nhuận cao nhất là \n'
                                %(latex(a),latex(b),latex(c),latex(d),latex(e)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai = ('Gọi $x$ đồng là số tiền mà doanh nghiệp dự định giảm giá $(0 \\le x \\le %s)$. \\\\ \n'
                        'Khi đó \\\\ \n'
                        'Lợi nhuận thu được khi bán một chiếc xe là $%s-x-%s=%s-x$. \\\\ \n'
                        'Số xe mà doanh nghiệp sẽ bán được trong một năm là $%s+%s x$. \\\\ \n'
                        'Lợi nhuận mà doanh nghiệp thu dược trong một năm là \n'
                        '$$f(x)=(%s-x)(%s+%s x)=%s.$$ \n'
                        'Xét hàm số $f(x)=%s$ trên đoạn $[0;%s]$. \\\\ \n'
                        'Đồ thị hàm số là một parabol có đỉnh là $\\left(%s; %s \\right)$. \\\\ \n'
                        'Suy ra hàm số đạt giá trị lớn nhất bằng $%s$ khi $x=%s$. \\\\ \n'
                        'Tức là khi giảm giá mỗi xe đi $%s$ triệu đồng thì số xe bán ra được nhiều nhất. \\\\ \n'
                        'Vậy giá mới của chiếc xe là $%s$ triệu dồng thì lợi nhuận thu được là cao nhất.'

                        %(latex(k),
                            latex(b),latex(a),latex(k),
                            latex(c),latex(e),
                            latex(k),latex(c),latex(e),latex(f),
                            latex(f),latex(k),
                            latex(x0),latex(f0),
                            latex(f0),latex(x0),
                            latex(xkq),
                            latex(ykq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

