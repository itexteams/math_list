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


def bt_dang3_p3_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xa=randint(-9,9)
                ya=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)

                while ya==0 or yb==0 or xa==xb:
                    x=symbols('x')
                    y=symbols('y')
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)

                x0=Rational((xb**2+yb**2-xa**2-ya**2),(2*(xb-xa)))
                bk=sqrt((x0-xa)**2+ya**2)
                number = Decimal(float(bk))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, đường tròn $(C)$ đi qua hai điểm $A(%s;%s),B(%s;%s)$ và có tâm $I$ thuộc trục hoành có bán kính bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)'

                                %(latex(xa),latex(ya),latex(xb),latex(yb))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi tâm $I(x;0)\\in Ox$. Ta có $\\vec{AI}=(x-%s;%s);\\vec{BI}=(x-%s;%s)$\\\\ \n'
                        '$IA^2=IB^2 \\Leftrightarrow (x-%s)^2+(%s)^2=(x-%s)^2+(%s)^2 \\Leftrightarrow x=%s$zzz Khi đó tâm $I\\left(%s;0\\right)$zzz\\\\ \n'
                        'Bán kính đường tròn $(C)$ là $R=AI=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s\\approx %s$zzz'



                        %(latex(xa),latex(-ya),latex(xb),latex(-yb),
                            latex(xa),latex(-ya),latex(xb),latex(-yb),latex(x0),latex(x0),
                            latex(x0),latex(xa),latex(-ya),latex(bk),latex(kq),
                            )
                        )

                #Đáp án
                dapan='  \\shortans[0]{$%s$}   \n'%(latex(kq))

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xa=randint(-9,9)
                ya=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)

                while xa==0 or xb==0 or ya==yb:
                    x=symbols('x')
                    y=symbols('y')
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)

                y0=Rational((xb**2+yb**2-xa**2-ya**2),(2*(yb-ya)))
                bk=sqrt((xa)**2+(y0-ya)**2)

                number = Decimal(float(bk))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, đường tròn $(C)$ đi qua hai điểm $A(%s;%s),B(%s;%s)$ và có tâm $I$ thuộc trục tung có bán kính bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)'

                                %(latex(xa),latex(ya),latex(xb),latex(yb))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi tâm $I(0;y)\\in Oy$. Ta có $\\vec{AI}=(%s;y-%s);\\vec{BI}=(%s;y-%s)$\\\\ \n'
                        '$IA^2=IB^2 \\Leftrightarrow (%s)^2+(y-%s)^2=(%s)^2+(y-%s)^2 \\Leftrightarrow y=%s$zzz Khi đó tâm $I\\left(0;%s\\right)$zzz\\\\ \n'
                        'Bán kính đường tròn $(C)$ là $R=AI=\\sqrt{(%s)^2+\\left(%s-%s\\right)^2}=%s\\approx %s$zzz'



                        %(latex(-xa),latex(ya),latex(-xb),latex(yb),
                            latex(-xa),latex(ya),latex(-xb),latex(yb),latex(y0),latex(y0),
                            latex(-xa),latex(y0),latex(ya),latex(bk),latex(kq)
                            )
                        )

                #Đáp án
                dapan='  \\shortans[0]{$%s$}   \n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('-+','-').replace('+-', '-').replace('--', '+').replace('.', ',').replace('zzz', '.')
            return content  

