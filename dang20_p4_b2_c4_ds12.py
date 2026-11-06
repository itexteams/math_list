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


def bt_dang20_p4_b2_c4_ds12(self):
            # Khai báo biến
            n=symbols('n')
            c=randint(3,20)
            v=randint(3,20)
            while c==v:
                c=randint(3,20)
                v=randint(3,20)
            n1=c+v
            p1=nsimplify(c/n1)
            p2=nsimplify((c-1)/(n1-1))
            p=p1*p2
            pt=p*n**2-p*n-c*(c-1)
            s=solve(pt,n)
            ss=sorted(s)
            k=c*(c-1)
            q1=c/n
            q2=(c-1)/(n-1)
            t=k/(n*(n-1))
            x1=ss[1]
            x2=ss[0]
            kq=n1
            lismau1=['vàng','cam','tím']
            lismau2=['xanh','đỏ']
            lismaut=['Đạo','Chiến','Hồng','Hương','Giang','Oanh','Hoa','Dương','Páo','Dũng','Hường','Chung']
            m1=random.choice(lismau1)
            m2=random.choice(lismau2)
            b=random.choice(lismaut)
            # Nội dung câu hỏi
            noidungcauhoi = ('Trong một túi có một số chiếc kẹo cùng loại, chỉ khác màu, trong đó có $%s$ kẹo màu %s, còn lại là kẹo màu %s, '
                            'bạn %s lấy ngẫu nhiên một cái kẹo từ trong túi, không trả lại. Sau đó bạn %s lại lấy ngẫu nhiên thêm một cái kẹo khác từ trong túi. '
                            'Biết rằng xác suất để bạn %s lấy được cả hai cái kẹo màu %s bằng $%s$. Hỏi ban đầu trong túi có bao nhiêu cái kẹo?'
                            %(latex(c),m1,m2,b,b,b,m1,latex(p))

                            )
            # Nội dung lời giải
            loigiai = ('Xét các biến cố:\\\\ \n'
                        '\\hspace*{1cm} $A$: "Lần thứ nhất bạn %s lấy được kẹo màu %s"\\\\ \n'
                    '\\hspace*{1cm} $B$: "Lần thứ hai bạn %s lấy được kẹo màu %s";\\\\ \n'
                    'Gọi số kẹo ban đầu trong túi là $n$ $(n \\in \\mathbb{N}, n>%s)$ ta có\\\\ \n'
                    'Theo bài ta có:\\\\ \n'
                    '\\hspace*{1cm}$\\mathrm{P}(A)=\\dfrac{%s}{n}$; $\\mathrm{P}(B|A)=\\dfrac{%s}{n-1}$\\\\ \n'
                    'Suy ra xác suất để cả hai lần lấy được kẹo màu %s là:\\\\ \n'
                    '\\hspace*{1cm}$\\mathrm{P}(AB)=\\mathrm{P}(A)\\cdot \\mathrm{P}(B|A)=\\dfrac{%s}{n}\\cdot\\dfrac{%s}{n-1}=\\dfrac{%s}{n(n-1)}$.\\\\ \n'
                    'Theo bài ta có:\\\\ \n'
                    '\\hspace*{1cm}$\\mathrm{P}(AB)=%s\\Leftrightarrow \\dfrac{%s}{n(n-1)}=%s\\Leftrightarrow %s=0\\Leftrightarrow \\hoac{&x=%s \\hspace*{0.3cm} \\text{(Thoả mãn)}\\\\&x=%s\\hspace*{0.3cm} \\text{(Loại)}}$.\\\\ \n'
                    'Vậy ban đầu trong túi có $%s$ cái kẹo.'
                        %(b,m1,b,m1,latex(c),latex(c),latex(c-1),m1,latex(c),latex(c-1),latex(c*(c-1)),latex(p),latex(k),latex(p),latex(pt),
                        latex(x1),latex(x2),latex(x1)
                        ))




            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content 

