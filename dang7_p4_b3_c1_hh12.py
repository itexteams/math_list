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


def bt_dang7_p4_b3_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                xa=randint(-15,15)
                ya=randint(-15,15)
                za=randint(-15,15)

                xb=randint(-15,15)
                yb=randint(-15,15)
                zb=randint(-15,15)

                xc=randint(-15,15)
                yc=randint(-15,15)
                zc=randint(-15,15)

                a=randint(1,3)
                b=randint(-4,4)
                c=randint(-5,5)

                while a+b+c<=0 or xa==xb==xc or ya==yb==yc or a*xa+b*xb+c*xc==0 or a*ya+b*yb+c*yc==0 or a*za+b*zb+c*zc==0 or a==0 or (a*ya+b*yb+c*yc)/(a+b+c)==ya==yb==yc or b==0 or c==0 or a==b==c or a==-b==c or (a*ya+b*yb+c*yc+a*xa+b*xb+c*xc)/(a+b+c)>=99 or (a*ya+b*yb+c*yc+a*xa+b*xb+c*xc)/(a+b+c)<=-9:
                    xa=randint(-15,15)
                    ya=randint(-15,15)
                    za=randint(-15,15)

                    xb=randint(-15,15)
                    yb=randint(-15,15)
                    zb=randint(-15,15)

                    xc=randint(-15,15)
                    yc=randint(-15,15)
                    zc=randint(-15,15)

                    a=randint(1,3)
                    b=randint(-4,4)
                    c=randint(-5,5)

                x1=nsimplify((a*xa+b*xb+c*xc)/(a+b+c))
                y1=nsimplify((a*ya+b*yb+c*yc)/(a+b+c))
                z1=nsimplify((a*za+b*zb+c*zc)/(a+b+c))

                kq1=nsimplify(x1+y1)



                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s),B(%s;%s;%s),C(%s;%s;%s)$$zz$ Gọi điểm $M(a;b;c)$ thuộc mặt phẳng $(Oxy)$ sao cho biểu thức $P=%s\\vec{MA}^2+%s\\vec{MB}^2+%s\\vec{MC}^2$ đạt giá trị nhỏ nhất$zz$ Tính giá trị của biểu thức $a+b+c$$zz$'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc),latex(a),latex(b),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $I(x;y;z)$ là điểm thoả mãn đẳng thức $%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}=\\vec{0}$$zz$\\\\ \n'
                        'Ta có\n'
                        '\\begin{eqnarray*}\n'
                        '%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}=\\vec{0} &\\Leftrightarrow& \\heva{&%s(%s-x)+%s(%s-x)+%s(%s-x)=0\\\\&%s(%s-y)+%s(%s-y)+%s(%s-y)=0\\\\&%s(%s-z)+%s(%s-z)+%s(%s-z)=0}\\\\ \n'
                        '&\\Leftrightarrow&\\heva{&x=%s\\\\&y=%s\\\\&z=%s}$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Suy ra $I\\left(%s;%s;%s\\right)$$zz$\\\\ \n'
                        'Ta có\n'
                        '\\begin{eqnarray*}\n'
                        'P=%s\\vec{MA}^2+%s\\vec{MB}^2+%s\\vec{MC}^2&=&%s\\left(\\vec{MI}+\\vec{IA}\\right)^2+%s\\left(\\vec{MI}+\\vec{IB}\\right)^2+%s\\left(\\vec{MI}+\\vec{IC}\\right)^2\\\\ \n'
                        '&=&%s\\vec{MI}^2+%s\\vec{IA}^2+%s\\vec{IB}^2+%s\\vec{IC}^2+2\\vec{MI}\\left(%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}\\right)\\\\ \n'
                        '&=&%s\\vec{MI}^2+%s\\vec{IA}^2+%s\\vec{IB}^2+%s\\vec{IC}^2\\\\ \n'
                        '&=&%s\\abs{\\vec{MI}}^2+%s\\abs{\\vec{IA}}^2+%s\\abs{\\vec{IB}}^2+%s\\abs{\\vec{IC}}^2 \n'
                        '\\end{eqnarray*}\n'
                        'Vì các điểm $A,B,C,I$ cố định nên biểu thức $P$ nhỏ nhất khi $\\abs{\\vec{MI}}^2$ nhỏ nhất$zz$ Điều này xảy ra khi $M$ là hình chiếu của $I\\left(%s;%s;%s\\right)$ lên mặt phẳng $(Oxy)$$zz$\\\\ \n'
                        'Suy ra $M\\left(%s;%s;0\\right)$$zz$ Vậy $a+b+c=%s+%s+0=%s$$zz$'
                        %(latex(a),latex(b),latex(c),
                            latex(a),latex(b),latex(c),
                            latex(a),latex(xa),latex(b),latex(xb),latex(c),latex(xc),
                            latex(a),latex(ya),latex(b),latex(yb),latex(c),latex(yc),
                            latex(a),latex(za),latex(b),latex(zb),latex(c),latex(zc),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(y1),latex(z1),
                            latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(y1),latex(x1),latex(y1),latex(kq1)
                            )
                        )

                #Đáp án

            if dang=='2':
                xa=randint(-15,15)
                ya=randint(-15,15)
                za=randint(-15,15)

                xb=randint(-15,15)
                yb=randint(-15,15)
                zb=randint(-15,15)

                xc=randint(-15,15)
                yc=randint(-15,15)
                zc=randint(-15,15)

                a=randint(1,3)
                b=randint(-4,4)
                c=randint(-5,5)

                while a+b+c<=0 or xa==xb==xc or ya==yb==yc or a*xa+b*xb+c*xc==0 or a*ya+b*yb+c*yc==0 or a*za+b*zb+c*zc==0 or a==0 or (a*ya+b*yb+c*yc)/(a+b+c)==ya==yb==yc or b==0 or c==0 or a==b==c or a==-b==c or (a*za+b*zb+c*zc+a*xa+b*xb+c*xc)/(a+b+c)>=99 or (a*za+b*zb+c*zc+a*xa+b*xb+c*xc)/(a+b+c)<=-9:
                    xa=randint(-15,15)
                    ya=randint(-15,15)
                    za=randint(-15,15)

                    xb=randint(-15,15)
                    yb=randint(-15,15)
                    zb=randint(-15,15)

                    xc=randint(-15,15)
                    yc=randint(-15,15)
                    zc=randint(-15,15)

                    a=randint(1,3)
                    b=randint(-4,4)
                    c=randint(-5,5)

                x1=nsimplify((a*xa+b*xb+c*xc)/(a+b+c))
                y1=nsimplify((a*ya+b*yb+c*yc)/(a+b+c))
                z1=nsimplify((a*za+b*zb+c*zc)/(a+b+c))

                kq1=nsimplify(x1+z1)



                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s),B(%s;%s;%s),C(%s;%s;%s)$$zz$ Gọi điểm $M(a;b;c)$ thuộc mặt phẳng $(Oxz)$ sao cho biểu thức $P=%s\\vec{MA}^2+%s\\vec{MB}^2+%s\\vec{MC}^2$ đạt giá trị nhỏ nhất$zz$ Tính giá trị của biểu thức $a+b+c$$zz$'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc),latex(a),latex(b),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $I(x;y;z)$ là điểm thoả mãn đẳng thức $%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}=\\vec{0}$$zz$\\\\ \n'
                        'Ta có\n'
                        '\\begin{eqnarray*}\n'
                        '%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}=\\vec{0} &\\Leftrightarrow& \\heva{&%s(%s-x)+%s(%s-x)+%s(%s-x)=0\\\\&%s(%s-y)+%s(%s-y)+%s(%s-y)=0\\\\&%s(%s-z)+%s(%s-z)+%s(%s-z)=0}\\\\ \n'
                        '&\\Leftrightarrow&\\heva{&x=%s\\\\&y=%s\\\\&z=%s}$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Suy ra $I\\left(%s;%s;%s\\right)$$zz$\\\\ \n'
                        'Ta có\n'
                        '\\begin{eqnarray*}\n'
                        'P=%s\\vec{MA}^2+%s\\vec{MB}^2+%s\\vec{MC}^2&=&%s\\left(\\vec{MI}+\\vec{IA}\\right)^2+%s\\left(\\vec{MI}+\\vec{IB}\\right)^2+%s\\left(\\vec{MI}+\\vec{IC}\\right)^2\\\\ \n'
                        '&=&%s\\vec{MI}^2+%s\\vec{IA}^2+%s\\vec{IB}^2+%s\\vec{IC}^2+2\\vec{MI}\\left(%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}\\right)\\\\ \n'
                        '&=&%s\\vec{MI}^2+%s\\vec{IA}^2+%s\\vec{IB}^2+%s\\vec{IC}^2\\\\ \n'
                        '&=&%s\\abs{\\vec{MI}}^2+%s\\abs{\\vec{IA}}^2+%s\\abs{\\vec{IB}}^2+%s\\abs{\\vec{IC}}^2 \n'
                        '\\end{eqnarray*}\n'
                        'Vì các điểm $A,B,C,I$ cố định nên biểu thức $P$ nhỏ nhất khi $\\abs{\\vec{MI}}^2$ nhỏ nhất$zz$ Điều này xảy ra khi $M$ là hình chiếu của $I\\left(%s;%s;%s\\right)$ lên mặt phẳng $(Oxz)$$zz$\\\\ \n'
                        'Suy ra $M\\left(%s;0;%s\\right)$$zz$ Vậy $a+b+c=%s+0+%s=%s$$zz$'
                        %(latex(a),latex(b),latex(c),
                            latex(a),latex(b),latex(c),
                            latex(a),latex(xa),latex(b),latex(xb),latex(c),latex(xc),
                            latex(a),latex(ya),latex(b),latex(yb),latex(c),latex(yc),
                            latex(a),latex(za),latex(b),latex(zb),latex(c),latex(zc),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(y1),latex(z1),
                            latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(z1),latex(x1),latex(z1),latex(kq1)
                            )
                        )

                #Đáp án

            if dang=='3':
                xa=randint(-15,15)
                ya=randint(-15,15)
                za=randint(-15,15)

                xb=randint(-15,15)
                yb=randint(-15,15)
                zb=randint(-15,15)

                xc=randint(-15,15)
                yc=randint(-15,15)
                zc=randint(-15,15)

                a=randint(1,3)
                b=randint(-4,4)
                c=randint(-5,5)

                while a+b+c<=0 or xa==xb==xc or ya==yb==yc or a*xa+b*xb+c*xc==0 or a*ya+b*yb+c*yc==0 or a*za+b*zb+c*zc==0 or a==0 or (a*ya+b*yb+c*yc)/(a+b+c)==ya==yb==yc or b==0 or c==0 or a==b==c or a==-b==c or (a*ya+b*yb+c*yc+a*za+b*zb+c*zc)/(a+b+c)>=99 or (a*ya+b*yb+c*yc+a*za+b*zb+c*zc)/(a+b+c)<=-9:
                    xa=randint(-15,15)
                    ya=randint(-15,15)
                    za=randint(-15,15)

                    xb=randint(-15,15)
                    yb=randint(-15,15)
                    zb=randint(-15,15)

                    xc=randint(-15,15)
                    yc=randint(-15,15)
                    zc=randint(-15,15)

                    a=randint(1,3)
                    b=randint(-4,4)
                    c=randint(-5,5)

                x1=nsimplify((a*xa+b*xb+c*xc)/(a+b+c))
                y1=nsimplify((a*ya+b*yb+c*yc)/(a+b+c))
                z1=nsimplify((a*za+b*zb+c*zc)/(a+b+c))

                kq1=nsimplify(z1+y1)



                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s),B(%s;%s;%s),C(%s;%s;%s)$$zz$ Gọi điểm $M(a;b;c)$ thuộc mặt phẳng $(Oyz)$ sao cho biểu thức $P=%s\\vec{MA}^2+%s\\vec{MB}^2+%s\\vec{MC}^2$ đạt giá trị nhỏ nhất$zz$ Tính giá trị của biểu thức $a+b+c$$zz$'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc),latex(a),latex(b),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $I(x;y;z)$ là điểm thoả mãn đẳng thức $%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}=\\vec{0}$$zz$\\\\ \n'
                        'Ta có\n'
                        '\\begin{eqnarray*}\n'
                        '%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}=\\vec{0} &\\Leftrightarrow& \\heva{&%s(%s-x)+%s(%s-x)+%s(%s-x)=0\\\\&%s(%s-y)+%s(%s-y)+%s(%s-y)=0\\\\&%s(%s-z)+%s(%s-z)+%s(%s-z)=0}\\\\ \n'
                        '&\\Leftrightarrow&\\heva{&x=%s\\\\&y=%s\\\\&z=%s}$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Suy ra $I\\left(%s;%s;%s\\right)$$zz$\\\\ \n'
                        'Ta có\n'
                        '\\begin{eqnarray*}\n'
                        'P=%s\\vec{MA}^2+%s\\vec{MB}^2+%s\\vec{MC}^2&=&%s\\left(\\vec{MI}+\\vec{IA}\\right)^2+%s\\left(\\vec{MI}+\\vec{IB}\\right)^2+%s\\left(\\vec{MI}+\\vec{IC}\\right)^2\\\\ \n'
                        '&=&%s\\vec{MI}^2+%s\\vec{IA}^2+%s\\vec{IB}^2+%s\\vec{IC}^2+2\\vec{MI}\\left(%s\\vec{IA}+%s\\vec{IB}+%s\\vec{IC}\\right)\\\\ \n'
                        '&=&%s\\vec{MI}^2+%s\\vec{IA}^2+%s\\vec{IB}^2+%s\\vec{IC}^2\\\\ \n'
                        '&=&%s\\abs{\\vec{MI}}^2+%s\\abs{\\vec{IA}}^2+%s\\abs{\\vec{IB}}^2+%s\\abs{\\vec{IC}}^2 \n'
                        '\\end{eqnarray*}\n'
                        'Vì các điểm $A,B,C,I$ cố định nên biểu thức $P$ nhỏ nhất khi $\\abs{\\vec{MI}}^2$ nhỏ nhất$zz$ Điều này xảy ra khi $M$ là hình chiếu của $I\\left(%s;%s;%s\\right)$ lên mặt phẳng $(Oyz)$$zz$\\\\ \n'
                        'Suy ra $M\\left(0;%s;%s\\right)$$zz$ Vậy $a+b+c=0+%s+%s=%s$$zz$'
                        %(latex(a),latex(b),latex(c),
                            latex(a),latex(b),latex(c),
                            latex(a),latex(xa),latex(b),latex(xb),latex(c),latex(xc),
                            latex(a),latex(ya),latex(b),latex(yb),latex(c),latex(yc),
                            latex(a),latex(za),latex(b),latex(zb),latex(c),latex(zc),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(y1),latex(z1),
                            latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),
                            latex(a+b+c),latex(a),latex(b),latex(c),
                            latex(x1),latex(y1),latex(z1),
                            latex(y1),latex(z1),latex(y1),latex(z1),latex(kq1)
                            )
                        )

                #Đáp án

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-').replace('1\\vec', '\\vec').replace('.', ',').replace('$zz$', '.').replace('1(', '(').replace('1\\left(', '\\left(').replace('\\text{-', '\\text{$-$').replace('+1\\abs', '+\\abs').replace('-1\\abs', '-\\abs')
            return content

