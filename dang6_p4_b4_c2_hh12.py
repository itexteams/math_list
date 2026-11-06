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


def bt_dang6_p4_b4_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')
                t=symbols('t')
                a1=randint(-3,3)
                a2=randint(-3,3)
                a3=randint(-3,3)
                b1=randint(-3,3)
                b2=randint(-3,3)
                b3=randint(-3,3)
                x0=randint(-3,3)
                y0=randint(-3,3)
                z0=randint(-3,3)
                a=randint(-3,3)
                b=randint(-3,3)
                c=randint(-3,3)
                while a1**2+a2**2+a3**2==0 or b1**2+b2**2+b3**2==0 or 2*a1-2*b1==0 or a==0 or b==0 or c==0 or 2*a*(x0-a1)+2*b*(y0-a2)+2*c*(z0-a3)-2*a*(x0-b1)-2*b*(y0-b2)-2*c*(z0-b3)==0:
                    x=symbols('x')
                    y=symbols('y')
                    z=symbols('z')
                    t=symbols('t')
                    a1=randint(-3,3)
                    a2=randint(-3,3)
                    a3=randint(-3,3)
                    b1=randint(-3,3)
                    b2=randint(-3,3)
                    b3=randint(-3,3)
                    x0=randint(-3,3)
                    y0=randint(-3,3)
                    z0=randint(-3,3)
                    a=randint(-3,3)
                    b=randint(-3,3)
                    c=randint(-3,3)

                xa=x0-a1
                ya=y0-a2
                za=z0-a3

                xb=x0-b1
                yb=y0-b2
                zb=z0-b3

                at=2*a*xa+2*b*ya+2*c*za-2*a*xb-2*b*yb-2*c*zb
                bt=xb**2+yb**2+zb**2-xa**2-ya**2-za**2
                t=Rational((xb**2+yb**2+zb**2-xa**2-ya**2-za**2),(2*a*xa+2*b*ya+2*c*za-2*a*xb-2*b*yb-2*c*zb))

                r=sqrt((xa+a*t)**2+(ya+b*t)**2+(za+c*t)**2)

                r1=sqrt((xa+a*t-1)**2+(ya+b*t-1)**2+(za+c*t)**2)
                r2=sqrt((xa+a*t+1)**2+(ya+b*t+1)**2+(za+c*t)**2)
                r3=sqrt((xa+a*t-2)**2+(ya+b*t-2)**2+(za+c*t)**2)
                r4=sqrt((xa+a*t+2)**2+(ya+b*t+2)**2+(za+c*t)**2)



                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho mặt cầu $(S)$ đi qua 2 điểm $A(%s;%s;%s)$ và $B(%s;%s;%s)$, có tâm $I$ nằm trên đường thẳng $\\Delta: \\heva{&x=%s+%st \\\\&y=%s+%st \\\\&z=%s+%st}$. Tìm bán kính $R$ của mặt cầu $(S)$.'
                                %(latex(a1),latex(a2),latex(a3),latex(b1),latex(b2),latex(b3),latex(x0),latex(a),latex(y0),latex(b),latex(z0),latex(c)))

                # Nội dung lời giải
                loigiai = ('Vì mặt cầu tâm $I$ thuộc đường thẳng $\\Delta$ nên tâm có dạng $I(%s+%st;%s+%st;%s+%st).\\\\ \n'
                        '\\Rightarrow \\heva{&\\vec{IA}=(%s+%st;%s+%st;%s+%st)\\\\&\\vec{IB}=(%s+%st;%s+%st;%s+%st)}$.\\\\ \n'
                        'Mặt cầu đi qua $A(%s;%s;%s), B(%s;%s;%s)$, nên bán kính $R=IA=IB\\Rightarrow IA^2=IB^2$\\\\ \n'
                        '$\\Leftrightarrow (%s+%st)^2+(%s+%st)^2+(%s+%st)^2=(%s+%st)^2+(%s+%st)^2+(%s+%st)^2 \\Leftrightarrow %st+%s=0 \\Leftrightarrow t=%s$.\\\\ \n'
                        '$\\Rightarrow \\vec{IA}=\\left(%s;%s;%s\\right)$.\\\\ \n'
                        'Khi đó bán kính mặt cầu $(S)$ là $R=IA=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2+\\left(%s\\right)^2}=%s$.'

                        %(latex(x0),latex(a),latex(y0),latex(b),latex(z0),latex(c),

                        latex(xa),latex(a),latex(ya),latex(b),latex(za),latex(c),latex(xb),latex(a),latex(yb),latex(b),latex(zb),latex(c),
                        latex(a1),latex(a2),latex(a3),latex(b1),latex(b2),latex(b3),
                        latex(xa),latex(a),latex(ya),latex(b),latex(za),latex(c),latex(xb),latex(a),latex(yb),latex(b),latex(zb),latex(c), latex(at),latex(-bt),latex(t),
                        latex(xa+a*t),latex(ya+b*t),latex(za+c*t),
                        latex(xa+a*t),latex(ya+b*t),latex(za+c*t),latex(r),
                        )
                        )



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content  

