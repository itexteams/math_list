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


def bt_dang1_p4_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-6,6)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-6,6)
                u1=xb-xa
                u2=yb-ya
                u3=zb-za
                dk=gcd(gcd(u1,u2),u3)
                while xa==0 or ya==0 or za==0 or xa==xb or ya==yb or za==zb or dk!=1:
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-6,6)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-6,6)
                    u1=xb-xa
                    u2=yb-ya
                    u3=zb-za
                    dk=gcd(gcd(u1,u2),u3)


                # Nội dung câu hỏi
                noidungcauhoi =('Trong không gian $Oxyz$, cho hai điểm $A(%s;%s;%s),B(%s;%s;%s)$. Viết phương trình đường thẳng đi qua hai điểm $A,B$.'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có $\\vec{AB}=(%s;%s;%s)$.\\\\ \n'
                        'Đường thẳng $AB$ đi qua $A(%s;%s;%s)$ nhận $\\vec{AB}=(%s;%s;%s)$ làm vectơ chỉ phương có phương trình là '
                        '$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}.$'
                                %(latex(u1),latex(u2),latex(u3),
                                latex(xa),latex(ya),latex(za),
                                latex(u1),latex(u2),latex(u3),
                                latex(xa),latex(u1),latex(ya),latex(u2),latex(za),latex(u3),
                                ))

            if dang=='2':
                # Khai báo biến
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-6,6)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-6,6)
                u1=xb-xa
                u2=yb-ya
                u3=zb-za
                dk=gcd(gcd(u1,u2),u3)
                while xa==0 or ya==0 or za==0 or xa==xb or ya==yb or za==zb or dk!=1:
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-6,6)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-6,6)
                    u1=xb-xa
                    u2=yb-ya
                    u3=zb-za
                    dk=gcd(gcd(u1,u2),u3)


                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho hai điểm $A(%s;%s;%s),B(%s;%s;%s)$. Viết phương trình tham số của đường thẳng đi qua hai điểm $A,B$.'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb))
                                )

                # Nội dung lời giải
                loigiai =('Ta có $\\vec{AB}=(%s;%s;%s)$.\\\\ \n'
                        'Đường thẳng $AB$ đi qua $A(%s;%s;%s)$ nhận $\\vec{AB}=(%s;%s;%s)$ làm vectơ chỉ phương có phương trình tham số là '
                        '$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}.$'
                                %(latex(u1),latex(u2),latex(u3),
                                latex(xa),latex(ya),latex(za),
                                latex(u1),latex(u2),latex(u3),
                                latex(xa),latex(u1),latex(ya),latex(u2),latex(za),latex(u3),


                                )
                            )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('+-','-').replace('\\frac','\\dfrac').replace('+1t','+t').replace('-1t','-t')
            return content

