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


def bt_dang7_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                p1=randint(-5,5)
                p2=randint(-5,5)
                p3=randint(-5,5)
                q1=randint(-5,5)
                q2=randint(-5,5)
                q3=randint(-5,5)
                d1=randint(-5,5)
                d2=randint(-5,5)
                pt1=p1*x+p2*y+p3*z+d1
                pt2=q1*x+q2*y+q3*z+d2
                dk1=pt1.subs((x,y,z),(xa,ya,za))
                dk2=pt2.subs((x,y,z),(xa,ya,za))
                a1=p2*q3-p3*q2
                a2=p3*q1-q3*p1
                a3=p1*q2-p2*q1
                e=-(a1*xa+a2*ya+a3*za)
                u=gcd(gcd(a1,a2),a3)
                a=nsimplify(a1/u)
                b=nsimplify(a2/u)
                c=nsimplify(a3/u)
                d=nsimplify(e/u)
                pt=a*x+b*y+c*z+d
                while p1**2+p2**2+p3**2==0 or q1**2+q2**2+q3**2==0 or q1==0 or q2==0 or dk1==0 or dk2==0 or a1==0 or a2==0 or a3==0 or p1/q1==p2/q2:
                    x,y,z=symbols('x,y,z')
                    xa=randint(-8,8)
                    ya=randint(-8,8)
                    za=randint(-5,5)
                    p1=randint(-5,5)
                    p2=randint(-5,5)
                    p3=randint(-5,5)
                    q1=randint(-5,5)
                    q2=randint(-5,5)
                    q3=randint(-5,5)
                    d1=randint(-5,5)
                    d2=randint(-5,5)
                    pt1=p1*x+p2*y+p3*z+d1
                    pt2=q1*x+q2*y+q3*z+d2
                    dk1=pt1.subs((x,y,z),(xa,ya,za))
                    dk2=pt2.subs((x,y,z),(xa,ya,za))
                    a1=p2*q3-p3*q2
                    a2=p3*q1-q3*p1
                    a3=p1*q2-p2*q1
                    e=-(a1*xa+a2*ya+a3*za)
                    u=gcd(gcd(a1,a2),a3)
                    a=nsimplify(a1/u)
                    b=nsimplify(a2/u)
                    c=nsimplify(a3/u)
                    d=nsimplify(e/u)
                    pt=a*x+b*y+c*z+d


                # Nội dung câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, viết phương trình mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và đồng thời vuông góc với cả hai mặt phẳng $(P):%s=0, (Q):%s=0$. '
                                %(latex(xa),latex(ya),latex(za),latex(pt1),latex(pt2)))

                # Nội dung lời giải
                loigiai = ('Vectơ pháp tuyến của hai mặt phẳng $(P),(Q)$ lần lượt là $\\vec{n_p}=(%s;%s;%s)$ và $\\vec{n_q}=(%s;%s;%s)$.\\\\ \n'
                        'Vì mặt phẳng $(\\alpha)$ đồng thời vuông góc với hai mặt phẳng $(P)$ và $(Q)$ nên có một vec tơ pháp tuyến là\\\\ \n'
                        '$$\\vec{n}=[\\vec{n_p},\\vec{n_q}]=(%s;%s;%s).$$'
                        'Mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và nhận $\\vec{n}=(%s;%s;%s)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$%s(x-%s)+%s(y-%s)+%s(z-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy phương trình mặt phẳng $(\\alpha)$ là $%s=0$.'

                        %(latex(p1),latex(p2),latex(p3),
                        latex(q1),latex(q2),latex(q3),
                        latex(a1),latex(a2),latex(a3),
                        latex(xa),latex(ya),latex(za),
                        latex(a1),latex(a2),latex(a3),
                        latex(a1),latex(xa),latex(a2),latex(ya),latex(a3),latex(za),
                        latex(pt),latex(pt),


                        )
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-').replace('+1\\cdot','+').replace('+-','-').replace('-1\\cdot','-').replace('$$1\\cdot','').replace('$$-1\\cdot','-')
            return content 

