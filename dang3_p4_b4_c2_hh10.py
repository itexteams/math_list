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


def bt_dang3_p4_b4_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
            # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                c=dab+dac+dbc
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0 or c>=99:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                    dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                    dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                    dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                    c=dab+dac+dbc
                number = Decimal(float(c))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính chu vi của tam giác $ABC$$zz$ (kết quả làm tròn đến hàng phần chục)$zz$ \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $AB=\\abs{\\vec{AB}}=\\sqrt{(%s-%s)^2+(%s-%s)^2}=%s$$zz$\\\\ \n'
                                '\\hspace*{1cm} $AC=\\abs{\\vec{AC}}=\\sqrt{(%s-%s)^2+(%s-%s)^2}=%s$$zz$\\\\ \n'
                                '\\hspace*{1cm} $BC=\\abs{\\vec{BC}}=\\sqrt{(%s-%s)^2+(%s-%s)^2}=%s$$zz$\\\\ \n'
                                'Suy ra chu vi tam giác $ABC$ là\\\\ \n'
                                '\\hspace*{1cm} $P_{\\triangle ABC} = AB+AC+BC=%s+%s+%s \\approx %s$$zz$'
                                %(latex(x2),latex(x1),latex(y2),latex(y1),latex(dab),
                                latex(x3),latex(x1),latex(y3),latex(y1),latex(dac),
                                latex(x3),latex(x2),latex(y3),latex(y2),latex(dbc),
                                latex(dab),latex(dac),latex(dbc),latex(kq)
                                )
                            )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('--', '+').replace('+-', '-')
            return content     

