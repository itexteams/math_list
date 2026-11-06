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


def bt_dang4_p3_b1_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                #Khai báo biến
                x=symbols('x')
                y=symbols('y')
                a1=randint(-9,9)
                b1=randint(-9,9)

                t=randint(1,9)

                xa=randint(-9,9)
                ya=randint(-9,9)

                xm=randint(-9,9)
                ym=randint(-9,9)

                while a1==0 or b1==0 or a1==b1 or ya==0 or a1/b1==xa/ya:
                    x=symbols('x')
                    y=symbols('y')
                    a1=randint(-9,9)
                    b1=randint(-9,9)

                    t=randint(1,9)

                    xa=randint(-9,9)
                    ya=randint(-9,9)

                    xm=randint(-9,9)
                    ym=randint(-9,9)



                dtm1=-b1*x+a1*y+b1*xa-a1*ya
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd(-b1,a1),(b1*xa-a1*ya))
                # Rút gọn các hệ số
                hs_a1 = -b1// gcd
                hs_b1 = a1 // gcd
                hs_c1 = (b1*xa-a1*ya) // gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dtm = hs_a1*x+hs_b1*y+hs_c1

                xb=xa+a1*t
                yb=ya+b1*t
                qd=sqrt((xb-xa)**2+(yb-ya)**2)
                qds=sqrt((xb-xa)**2+(yb-ya)**2+1)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chuyển động của vật thể $M$ được thể hiện trên mặt phẳng tọa độ $(Oxy)$. Vật thể $M$ khởi hành từ điểm $A(%s;%s)$ và chuyển động thẳng đều với vectơ vận tốc là $\\vec{v}=(%s;%s)$. '
                                'Khi đó $M$ chuyển động trên đường thẳng $%s x+by+c=0$. Tổng $b+c$ bằng bao nhiêu?'
                                %(latex(xa),latex(ya),latex(a1),latex(b1),latex(hs_a1),))

                # Nội dung lời giải
                loigiai = ('Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể $M$ là $\\vec{v}=(%s;%s)$, do đó đường thẳng này có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$.'
                                ' Mặt khác đường thằng này đi qua điểm $A(%s;%s)$ nên có phương trình $%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0\\Rightarrow b=%s;c=%s$.\\\\ \n'
                                'Vậy $b+c=%s$.'
                                %(latex(a1),latex(b1),latex(-b1),latex(a1),latex(xa),latex(ya), latex(-b1),latex(xa),latex(a1),latex(ya),latex(dtm),latex(hs_b1),latex(hs_c1),
                                latex(hs_b1+hs_c1))
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(hs_b1+hs_c1))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('-+','-').replace('+-', '-').replace('--', '+').replace('11 x', '11f x').replace('1 x', 'x').replace('11f x', '11 x').replace('11 y', '11f y').replace('1 y', 'y').replace('11f y', '11 y')
            return content                

