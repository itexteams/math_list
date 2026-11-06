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


def bt_dang3_p1_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-9,9)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}>%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}>%s \\Leftrightarrow %s>{{\\log }_{%s}}(%s) \\Leftrightarrow %s>%s\\Leftrightarrow x>%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(%s;+\\infty\\right)$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-9,9)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}\\ge%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}\\ge%s \\Leftrightarrow %s\\ge{{\\log }_{%s}}(%s) \\Leftrightarrow %s\\ge%s\\Leftrightarrow x\\ge%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left[%s;+\\infty\\right)$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right)$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}<%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}<%s \\Leftrightarrow %s<{{\\log }_{%s}}(%s) \\Leftrightarrow %s<%s\\Leftrightarrow x<%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right)$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right]$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}\\le%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}\\le%s \\Leftrightarrow %s\\le{{\\log }_{%s}}(%s) \\Leftrightarrow %s\\le%s\\Leftrightarrow x\\le%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right]$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}<%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}<%s \\Leftrightarrow %s<{{\\log }_{%s}}(%s) \\Leftrightarrow %s<%s\\Leftrightarrow x>%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(%s;+\\infty\\right)$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}\\le%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}\\le%s \\Leftrightarrow %s\\le{{\\log }_{%s}}(%s) \\Leftrightarrow %s\\le%s\\Leftrightarrow x\\ge%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left[%s;+\\infty\\right)$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right)$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}>%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}>%s \\Leftrightarrow %s>{{\\log }_{%s}}(%s) \\Leftrightarrow %s>%s\\Leftrightarrow x<%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right)$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='8':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,7)
                while A==0:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,7)
                fx=A*x+B
                b=a**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right]$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{%s}^{%s}}\\ge%s$ là  \n'
                                %(latex(a),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{%s}^{%s}}\\ge%s \\Leftrightarrow %s\\ge{{\\log }_{%s}}(%s) \\Leftrightarrow %s\\ge%s\\Leftrightarrow x\\le%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right]$. \n'
                        %(latex(a),latex(fx),latex(b),latex(fx),latex(a),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='9':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right)$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}>%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}>%s \\Leftrightarrow %s<{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s<%s\\Leftrightarrow x<%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right)$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='10':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-19,19)
                    a=randint(2,6)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right]$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}\\ge%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}\\ge%s \\Leftrightarrow %s\\le{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s\\le%s\\Leftrightarrow x\\le%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right]$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='11':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}<%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}<%s \\Leftrightarrow %s>{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s>%s\\Leftrightarrow x>%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(%s;+\\infty\\right)$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='12':
                # Khai báo biến
                x=symbols('x')
                A=randint(1,9)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(1,9)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}\\le%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}\\le%s \\Leftrightarrow %s\\ge{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s\\ge%s\\Leftrightarrow x\\ge%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left[%s;+\\infty\\right)$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='13':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}>%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}>%s \\Leftrightarrow %s<{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s<%s\\Leftrightarrow x>%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(%s;+\\infty\\right)$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='14':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left[%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty\\right)$'%(latex(n0+s1)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s2)),
                    '$\\left[%s;+\\infty\\right)$'%(latex(n0+s3)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}\\ge%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}\\ge%s \\Leftrightarrow %s\\le{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s\\le%s\\Leftrightarrow x\\ge%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left[%s;+\\infty\\right)$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='15':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right)$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}<%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}<%s \\Leftrightarrow %s>{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s>%s\\Leftrightarrow x<%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right)$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

            if dang=='16':
                # Khai báo biến
                x=symbols('x')
                A=randint(-9,-1)
                B=randint(-19,19)
                a=randint(2,7)
                c=randint(1,4)
                d=randint(1,5)
                g=randint(2,6)
                while A==0 or d>=g:
                    x=symbols('x')
                    A=randint(-9,-1)
                    B=randint(-19,19)
                    a=randint(2,7)
                    c=randint(1,4)
                    d=randint(1,5)
                    g=randint(2,6)
                e=Rational(d,g)
                fx=A*x+B
                b=e**c
                n0=Rational(c-B,A)
                dasai1=[-1,1]
                dasai2=[-2,2]
                dasai3=[-3,3]
                s1=random.choice(dasai1)
                s2=random.choice(dasai2)
                s3=random.choice(dasai3)
                du = ['$\\left(-\\infty;%s\\right]$'%(latex(n0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(-\\infty;%s\\right]$'%(latex(n0+s1)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s2)),
                    '$\\left(-\\infty;%s\\right]$'%(latex(n0+s3)),
                    '$\\left(-\\infty;%s\\right)$'%(latex(n0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập nghiệm của bất phương trình ${{\\left(%s\\right)}^{%s}}\\le%s$ là  \n'
                                %(latex(e),latex(fx),
                                latex(b)
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
                loigiai=('Bất phương trình ${{\\left(%s\\right)}^{%s}}\\le%s \\Leftrightarrow %s\\ge{{\\log }_{%s}}\\left(%s\\right) \\Leftrightarrow %s\\ge%s\\Leftrightarrow x\\le%s$.\\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s\\right]$. \n'
                        %(latex(e),latex(fx),latex(b),latex(fx),latex(e),latex(b),latex(fx),latex(c),latex(n0),latex(n0))
                        )

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

