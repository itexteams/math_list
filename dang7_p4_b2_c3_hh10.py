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


def bt_dang7_p4_b2_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xm=randint(-9,9)
                ym=randint(-9,9)
                xn=randint(-9,9)
                yn=randint(-9,9)

                xa=randint(-9,9)
                ya=randint(-9,9)

                xb=2*xm-xa
                yb=2*ym-ya
                xc=2*xn-xa
                yc=2*yn-ya

                while xc==xa or yc==ya or (xb-xa)/(xc-xa)==(yb-ya)/(yc-ya):
                    x=symbols('x')
                    y=symbols('y')
                    xm=randint(-9,9)
                    ym=randint(-9,9)
                    xn=randint(-9,9)
                    yn=randint(-9,9)

                    xa=randint(-9,9)
                    ya=randint(-9,9)

                    xb=2*xm-xa
                    yb=2*ym-ya
                    xc=2*xn-xa
                    yc=2*yn-ya

                ttab1=(xb-xa)*x+(yb-ya)*y-(xb-xa)*xm-(yb-ya)*ym
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xb-xa),(yb-ya)),-(xb-xa)*xm-(yb-ya)*ym)
                # Rút gọn các hệ số
                hs_a1 = (xb-xa) // gcd
                hs_b1 = (yb-ya) // gcd
                hs_c1 = (-(xb-xa)*xm-(yb-ya)*ym)// gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                ttab = hs_a1*x+hs_b1*y+hs_c1

                ttac1=(xc-xa)*x+(yc-ya)*y-(xc-xa)*xn-(yc-ya)*yn
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xc-xa),(yc-ya)),-(xc-xa)*xn-(yc-ya)*yn)
                # Rút gọn các hệ số
                hs_a2 = (xc-xa) // gcd
                hs_b2 = (yc-ya) // gcd
                hs_c2 = (-(xc-xa)*xn-(yc-ya)*yn)// gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                ttac = hs_a2*x+hs_b2*y+hs_c2

                eq1 = Eq(hs_a1*x+hs_b1*y,-hs_c1)
                eq2 = Eq(hs_a2*x+hs_b2*y,-hs_c2)

                # Giải hệ phương trình
                solution = solve((eq1, eq2), (x, y))

                # Tách riêng nghiệm
                x_value = solution[x]
                y_value = solution[y]






                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ, một tín hiệu âm thanh phát đi từ một vị trí và được ba thiết bị ghi tín hiệu đặt tại ba vị trí $A(%s;%s),B(%s;%s),C(%s;%s)$ nhận được cùng một thời điểm. Tìm tọa độ vị trí phát tín hiệu âm thanh đó.'
                                %(latex(xa),latex(ya),latex(xb),latex(yb),latex(xc),latex(yc))
                                )

                # Nội dung lời giải
                loigiai = ('Vì ba thiết bị nhận được tín hiệu cùng một thời điểm nên vị trí phát tín hiệu đó cách đều ba vị trí ghi tín hiệu và đó là tâm đường tròn ngoại tiếp tam giác $ABC$.\\\\ \n'
                        'Gọi $M,N$ lần lượt là trung điểm của $AB,AC\\Rightarrow M(%s;%s),N(%s;%s)$ \\\\ \n'
                        'Đường trung trực $AB$ đi qua $M$ nhận $\\vec{AB}=(%s;%s)$ làm vectơ pháp tuyến có phương trình tổng quát là\\\\ \n'
                        '$%s(x-%s)+%s(y-%s)\\Leftrightarrow %s=0$  $(d_1)$.\\\\ \n '
                        'Đường trung trực $AC$ đi qua $N$ nhận $\\vec{AC}=(%s;%s)$ làm vectơ pháp tuyến có phương trình tổng quát là\\\\ \n'
                        '$%s(x-%s)+%s(y-%s)\\Leftrightarrow %s=0$  $(d_2)$.\\\\ \n '
                        'Tâm đường tròn ngoại tiếp là giao điểm của $(d_1)$ và $(d_2)$ có tọa độ là nghiệm của hệ\\\\ \n'
                        '$\\heva{& %s=0\\\\ & %s=0} \\Leftrightarrow \\heva {& x=%s\\\\ & y=%s}$.\\\\ \n'
                        'Vậy vị trí phát tín hiệu âm thanh có tọa độ là $(%s;%s)$.'
                        %(latex(xm),latex(ym),latex(xn),latex(yn),
                            latex(xb-xa),latex(yb-ya),
                            latex(xb-xa),latex(xm),latex(yb-ya),latex(ym),latex(ttab),

                            latex(xc-xa),latex(yc-ya),
                            latex(xc-xa),latex(xn),latex(yc-ya),latex(yn),latex(ttac),
                            latex(ttab),latex(ttac),latex(x_value),latex(y_value),
                            latex(x_value),latex(y_value),

                            )
                        )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-')
            return content 

