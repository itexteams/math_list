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


def bt_dang12_p1_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10']
            dang=random.choice(lisdang)
            if dang=='10':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                b=randint(1,9)
                f=cos(a*x+pi/b)


                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left[%s\\right]^2\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left[%s\\right]^2\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(0),latex(pi/(a+1))
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(0),latex(pi/(a+1)),latex(f)
                        ))

            if dang=='9':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                f=sin(a*x)



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left[%s\\right]^2\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left[%s\\right]^2\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(0),latex(pi/(a+1)),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(0),latex(pi/(a+1))
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(0),latex(pi/(a+1)),latex(f)
                        ))
            if dang=='8':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,9)

                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(\\log_%s x\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(a)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(\\log_%s x\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(a)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|\\log_%s x\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(a)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|\\log_%s x \\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(a)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi đường $y=\\log_%s x$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(a),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left( \\log_%s x \\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(a)
                        ))
            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                f=a**x



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
                        ))
            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                f=sqrt(x**2+a)



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
                        ))

            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                f=(x**2+a)/(x-a+1)



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
                        ))

            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                f=(x+a+1)/(x+a-1)



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
                        ))

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                f=x**a



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
                        ))

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                f=x**2+2*a



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
                        ))

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                f=x+a



                du = ['$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$'%(latex(a+1),latex(a+3),latex(f)),


                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Gọi $D$ là hình phẳng giới hạn bởi các đường $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$. Thể tích của khối tròn xoay tạo thành khi quay $D$ quanh trục $Ox$ là'
                                %(latex(f),latex(a+1),latex(a+3)
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
                loigiai=('Thể tích vật thể tròn xoay cần tìm là $V=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2\\text{d}x$.'
                        %(latex(a+1),latex(a+3),latex(f)
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

