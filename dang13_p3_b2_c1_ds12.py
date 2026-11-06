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


def bt_dang13_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(50,200)
                b=randint(9,20)
                lisc=[200,250,500]
                c=random.choice(lisc)
                d=randint(5,20)
                e=d*1000/c
                while (b*e-a)%(2*e)!=0:
                    a=randint(50,200)
                    b=randint(9,20)
                    lisc=[200,250,500]
                    c=random.choice(lisc)
                    d=randint(5,20)
                    e=d*1000/c

                vt1=(e*x+a)*(b-x)
                vp1=expand(vt1, x)
                daoham=-2*e*x+b*e-a

                x0=Rational(b*e-a,2*e)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một cửa hàng trung bình bán được $%s$ cái tivi mỗi tháng với $%s$ triệu đồng một cái. Chủ cửa hàng nhận thấy rằng, nếu giảm giá bán mỗi cái tivi $%s$ nghìn đồng thì số lượng tivi bán ra sẽ tăng thêm $%s$ cái mỗi tháng. Hỏi cửa hàng nên bán với giá bao nhiêu (triệu) để doanh thu cửa hàng là lớn nhất?  \n'
                                %(latex(a),latex(b),latex(c),latex(d)
                                ))

                # Nội dung lời giải
                loigiai = ('Giả sử cần giảm giá bán mỗi cái tivi là $x$ triệu đồng $(x<%s)$. \\\\ \n'
                        'Do giảm giá bán mỗi cái $%s$ nghìn đồng thì số lượng tivi bán ra sẽ tăng thêm $%s$ cái mỗi tháng nên số lượng tivi bán ra tăng lên bây giờ là $\\dfrac{%s x}{%s}=%s x$. \\\\ \n'
                        'Khi đó doanh thu một tháng của cửa hàng là $%s=%s$. \\\\ \n'
                        'Xét hàm số $f(x)=%s$ với $(x<%s)$.\\\\ \n'
                        'Ta có $f\'(x)=%s$; $f\'(x)=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                            '{$t$/0.7,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                        ' {$0$,$%s$,$%s$}  \n'
                            '\\tkzTabLine{,+,0,-,} \n'
                            '\\tkzTabVar{-/,+/,-/}  \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Từ bảng biến thiên ta thấy, để doanh thu cửa hàng đạt cao nhất thì giá bán mỗi cái tivi là $%s-%s=%s$ triệu đồng. \\\\ \n'

                        %(latex(b),latex(c),latex(d),
                            latex(d),latex(c/1000),latex(d*1000/c),
                            latex(vt1),latex(vp1),
                            latex(vp1), latex(b),
                            latex(daoham),latex(x0),
                            latex(x0),latex(b),
                            latex(b),latex(x0),latex(b-x0)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(b-x0))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content

