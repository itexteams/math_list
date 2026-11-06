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


def bt_dang11_p1_b2_c3_hh10(self):
            lisdang = ['2','1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                a1=randint(-9,9)
                b1=randint(-9,9)

                a2=randint(-9,9)
                b2=randint(-9,9)

                a3=randint(-9,9)
                b3=randint(-9,9)

                while b2==b3 or a3==a2 or (b2-b3)*a1+(a3-a2)*b1-(b2-b3)*a2-(a3-a2)*b2==0:
                    x=symbols('x')
                    y=symbols('y')
                    a1=randint(-9,9)
                    b1=randint(-9,9)

                    a2=randint(-9,9)
                    b2=randint(-9,9)

                    a3=randint(-9,9)
                    b3=randint(-9,9)

                dtbc1=(b2-b3)*x+(a3-a2)*y-(b2-b3)*a2-(a3-a2)*b2
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((b2-b3),(a3-a2)),-(b2-b3)*a2-(a3-a2)*b2)
                # Rút gọn các hệ số
                hs_a1 = (b2-b3) // gcd
                hs_b1 = (a3-a2) // gcd
                hs_c1 = (-(b2-b3)*a2-(a3-a2)*b2)// gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dtbc = hs_a1*x+hs_b1*y+hs_c1
                kc6=abs(hs_a1*a1+hs_b1*b1+hs_c1+1)/sqrt((hs_a1)**2+(hs_b1)**2)
                kc1=abs(hs_a1*a1+hs_b1*b1+hs_c1+2)/sqrt((hs_a1)**2+(hs_b1)**2)
                kc2=abs(hs_a1*a1+hs_b1*b1+hs_c1+3)/sqrt((hs_a1)**2+(hs_b1)**2)
                kc3=abs(hs_a1*a1+hs_b1*b1+hs_c1-1)/sqrt((hs_a1)**2+(hs_b1)**2)
                kc4=abs(hs_a1*a1+hs_b1*b1+hs_c1-2)/sqrt((hs_a1)**2+(hs_b1)**2)
                kc5=abs(hs_a1*a1+hs_b1*b1+hs_c1-2)/sqrt((hs_a1)**2+(hs_b1)**2)
                kc=abs(hs_a1*a1+hs_b1*b1+hs_c1)/sqrt((hs_a1)**2+(hs_b1)**2)

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho tam giác $ABC$ có $A(%s;%s)$, $B(%s;%s)$ và $C(%s;%s)$ độ dài đường cao kẻ từ đỉnh $A$ của tam giác $ABC$ là'
                                %(latex(a1),latex(b1),latex(a2),latex(b2),latex(a3),latex(b3))
                                )

                # Nội dung lời giải
                loigiai = (
                        'Đường thẳng $BC$ có một vectơ chỉ phương là $\\vec{BC}=(%s;%s)\\Rightarrow$ vectơ pháp tuyến của đường thẳng $BC$ là $\\vec{n}=(%s;%s)$.\\\\ \n'
                        'Đường thẳng $BC$ đi qua điểm $B(%s;%s)$ có một vectơ pháp tuyến $\\vec{n}=(%s;%s)$ có phương trình tổng quát là '
                        '$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy độ dài đường cao kẻ từ đỉnh $A$ của tam giác là khoảng cách từ điểm $A(%s;%s)$ đến đường thẳng $BC$ là '
                        '$d(A,BC)=\\dfrac{|%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s$.'
                        %(latex(a3-a2),latex(b3-b2),latex(b2-b3),latex(a3-a2),
                            latex(a2),latex(b2),latex(b2-b3),latex(a3-a2),

                            latex(b2-b3),latex(a2),latex(a3-a2),latex(b2),latex(dtbc),
                            latex(a1),latex(b1), 
                            latex(hs_a1),latex(a1),latex(hs_b1),latex(b1),latex(hs_c1),latex(hs_a1),latex(hs_b1),latex(kc),


                            )
                        )

                du = ['$%s$'%(latex(kc)),

                    ]
                da = random.choice(du)
                s = ['$%s$'%(latex(kc1)),
                    '$%s$'%(latex(kc2)),
                    '$%s$'%(latex(kc3)),
                    '$%s$'%(latex(kc4)),
                    '$%s$'%(latex(kc5)),
                    '$%s$'%(latex(kc6)),


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            if dang == '2':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                a1=randint(-9,9)
                b1=randint(-9,9)

                a2=randint(-9,9)
                b2=randint(-9,9)

                a3=randint(-9,9)
                b3=randint(-9,9)

                while b2==b3 or a3==a2 or (b1-b3)*a2+(a3-a1)*b2-(b1-b3)*a1-(a3-a1)*b1==0:
                    x=symbols('x')
                    y=symbols('y')
                    a1=randint(-9,9)
                    b1=randint(-9,9)

                    a2=randint(-9,9)
                    b2=randint(-9,9)

                    a3=randint(-9,9)
                    b3=randint(-9,9)

                dtbc1=(b1-b3)*x+(a3-a1)*y-(b1-b3)*a1-(a3-a1)*b1
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((b1-b3),(a3-a1)),-(b1-b3)*a1-(a3-a1)*b1)
                # Rút gọn các hệ số
                hs_a2 = (b1-b3) // gcd
                hs_b2 = (a3-a1) // gcd
                hs_c2 = (-(b1-b3)*a1-(a3-a1)*b1)// gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dtac = hs_a2*x+hs_b2*y+hs_c2

                kc0=abs(hs_a2*a2+hs_b2*b2+hs_c2)/sqrt((hs_a2)**2+(hs_b2)**2)
                kc1=abs(hs_a2*a2+hs_b2*b2+hs_c2+1)/sqrt((hs_a2)**2+(hs_b2)**2)
                kc2=abs(hs_a2*a2+hs_b2*b2+hs_c2+2)/sqrt((hs_a2)**2+(hs_b2)**2)
                kc3=abs(hs_a2*a2+hs_b2*b2+hs_c2+3)/sqrt((hs_a2)**2+(hs_b2)**2)
                kc4=abs(hs_a2*a2+hs_b2*b2+hs_c2-1)/sqrt((hs_a2)**2+(hs_b2)**2)
                kc5=abs(hs_a2*a2+hs_b2*b2+hs_c2-2)/sqrt((hs_a2)**2+(hs_b2)**2)
                kc6=abs(hs_a2*a2+hs_b2*b2+hs_c2-3)/sqrt((hs_a2)**2+(hs_b2)**2)

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho tam giác $ABC$ có $A(%s;%s)$, $B(%s;%s)$ và $C(%s;%s)$ độ dài đường cao kẻ từ đỉnh $B$ của tam giác $ABC$ là'
                                %(latex(a1),latex(b1),latex(a2),latex(b2),latex(a3),latex(b3))
                                )

                # Nội dung lời giải
                loigiai = (
                        'Đường thẳng $AC$ có một vectơ chỉ phương là $\\vec{AC}=(%s;%s)\\Rightarrow$ vectơ pháp tuyến của đường thẳng $AC$ là $\\vec{n}=(%s;%s)$.\\\\ \n'
                        'Đường thẳng $AC$ đi qua điểm $A(%s;%s)$ có một vectơ pháp tuyến $\\vec{n}=(%s;%s)$ có phương trình tổng quát là '
                        '$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy độ dài đường cao kẻ từ đỉnh $B$ của tam giác là khoảng cách từ điểm $B(%s;%s)$ đến đường thẳng $AC$ là '
                        '$d(B,AC)=\\dfrac{|%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s$.'
                        %(latex(a3-a1),latex(b3-b1),latex(b1-b3),latex(a3-a1),
                            latex(a1),latex(b1),latex(b1-b3),latex(a3-a1),

                            latex(b1-b3),latex(a1),latex(a3-a1),latex(b1),latex(dtac),
                            latex(a2),latex(b2), 
                            latex(hs_a2),latex(a2),latex(hs_b2),latex(b2),latex(hs_c2),latex(hs_a2),latex(hs_b2),latex(kc0),


                            )
                        )

                du = ['$%s$'%(latex(kc0)),

                    ]
                da = random.choice(du)
                s = ['$%s$'%(latex(kc1)),
                    '$%s$'%(latex(kc2)),
                    '$%s$'%(latex(kc3)),
                    '$%s$'%(latex(kc4)),
                    '$%s$'%(latex(kc5)),
                    '$%s$'%(latex(kc6)),


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) +
                    '\\choice \n'
                    '{'+str(list_1[1])+'}\n'
                    '{'+str(list_1[2])+'}\n'
                    '{'+str(list_1[3])+'}\n'
                    '{'+str(list_1[0])+'}\n'
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\pm 0', '0').replace('1{x}', '{x}').replace('+0', '').replace('-0', '')
            return content 

