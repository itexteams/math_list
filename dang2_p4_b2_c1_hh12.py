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


def bt_dang2_p4_b2_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                x1=randint(-8,8)
                y1=randint(-8,8)
                z1=randint(-8,8)
                x2=randint(-8,8)
                y2=randint(-8,8)
                z2=randint(-8,8)
                x3=randint(-8,8)
                y3=randint(-8,8)
                z3=randint(-8,8)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2+(z3-z1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2+(z3-z2)**2))
                hd=(y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
                td=(z2-z1)*(x3-x1)-(x2-x1)*(z3-z1)
                cd=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)


                while hd==0 or td==0 or cd==0:
                    x1=randint(-8,8)
                    y1=randint(-8,8)
                    z1=randint(-8,8)
                    x2=randint(-8,8)
                    y2=randint(-8,8)
                    z2=randint(-8,8)
                    x3=randint(-8,8)
                    y3=randint(-8,8)
                    z3=randint(-8,8)
                    hd=(y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
                    td=(z2-z1)*(x3-x1)-(x2-x1)*(z3-z1)
                    cd=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
                xd=x3-x2+x1
                yd=y3-y2+y1
                zd=z3-z2+z1



                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$. Xác định tọa độ điểm $D$ để tứ giác $ABCD$ là hình bình hành.\\\\ \n'
                                %(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x3),latex(y3),latex(z3))
                                )

                # Nội dung lời giải
                loigiai = ('Để tứ giác $ABCD$ là hình bình hành thì $\\vec{AD}=\\vec{BC}$.\\\\ \n'
                                'Theo bài ta có $\\vec{AD}=(x-%s;y-%s;z-%s)$ và $\\vec{BC}=(%s;%s;%s)$.\\\\ \n'
                                '\\hspace*{1cm}$\\vec{AD}=\\vec{BC} \\Leftrightarrow \\heva{x-%s=%s\\\\y-%s=%s\\\\z-%s=%s} \\Leftrightarrow \\heva{x=%s\\\\y=%s\\\\z=%s}$.\\\\ \n'
                                'Vậy $D(%s;%s;%s)$.'
                                %(latex(x1),latex(y1),latex(z1),latex(x3-x2),latex(y3-y2),latex(z3-z2),latex(x1),latex(x3-x2),latex(y1),latex(y3-y2),latex(z1),latex(x3-z2),
                                latex(xd),latex(yd),latex(zd),latex(xd),latex(yd),latex(zd))

                            )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('1\\vec','\\vec').replace('-1\\vec','-\\vec').replace('+-','-').replace('\\frac','\\dfrac').replace('--','+').replace('-0x','').replace('+0x','').replace('+0','').replace('-0','').replace('=0+','').replace('=0-','-')
            return content                  

