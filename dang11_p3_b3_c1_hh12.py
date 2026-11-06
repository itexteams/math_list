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


def bt_dang11_p3_b3_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                xa=randint(100,200)
                ya=randint(100,300)
                za=randint(30,80)
                xb=randint(100,200)
                yb=randint(100,200)
                zb=randint(30,80)
                d=sqrt((xa+xb)**2+(ya+yb)**2+(za-zb)**2)
                while d>=9990 or za==zb:
                    xa=randint(100,200)
                    ya=randint(100,300)
                    za=randint(30,80)
                    xb=randint(100,200)
                    yb=randint(100,200)
                    zb=randint(30,80)
                    d=sqrt((xa+xb)**2+(ya+yb)**2+(za-zb)**2)


                number = Decimal(float(d))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một người đứng ở mặt đất điều khiển hai flycam để phục vụ trong một chương trình của đài truyền hình$zz$ Flycam I ở vị trí $A$ cách vị trí điều khiển '
                                '$%s$ m về phía nam và $%s$ m về phía đông, đồng thời cách mặt đất $%s$ m$zz$ Flycam II ở vị trí $B$ cách vị trí điều khiển '
                                '$%s$m về phía bắc và $%s$ m về phía tây, đồng thời cách mặt đất $%s$ m$zz$ Chọn hệ trục tọa độ $Oxyz$ với gốc $O$ là vị trí người điều khiển, '
                                'mặt phẳng $(Oxy)$ trùng với mặt đất, trục $Ox$ có hướng trùng với hướng nam, trục $Oy$ có hướng trùng với hướng đông, trục $Oz$ vuông góc với mặt đất hướng lên bầu trời, '
                                'đơn vị trên mỗi trục tính theo mét$zz$ Khoảng cách giữa hai flycam đó bằng bao nhiêu mét (làm tròn kết quả đến hàng đơn vị)?'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb))
                                )

                # Nội dung lời giải
                loigiai = ('Vị trí $A,B$ có tọa độ lần lượt là: $(%s;%s;%s),(-%s;-%s;%s)$$zz$ Suy ra khoảng cách giữa hai flycam đó bằng:\\\\ \n'
                        '$$AB=\\sqrt{(-%s-%s)^2+(-%s-%s)^2+(%s-%s)^2}\\approx %s \\text{(m)}$zz$$$'
                        %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),
                            latex(xb),latex(xa),latex(yb),latex(ya),latex(zb),latex(za),latex(kq)

                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                xa=randint(100,200)
                ya=randint(100,300)
                za=randint(30,80)
                xb=randint(100,200)
                yb=randint(100,200)
                zb=randint(30,80)
                d=sqrt((xa+xb)**2+(ya+yb)**2+(za-zb)**2)
                while d>=9990 or za==zb:
                    xa=randint(100,200)
                    ya=randint(100,300)
                    za=randint(30,80)
                    xb=randint(100,200)
                    yb=randint(100,200)
                    zb=randint(30,80)
                    d=sqrt((xa+xb)**2+(ya+yb)**2+(za-zb)**2)


                number = Decimal(float(d))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một người đứng ở mặt đất điều khiển hai flycam để phục vụ trong một chương trình của đài truyền hình$zz$ Flycam I ở vị trí $A$ cách vị trí điều khiển '
                                '$%s$ m về phía bắc và $%s$ m về phía đông, đồng thời cách mặt đất $%s$ m$zz$ Flycam II ở vị trí $B$ cách vị trí điều khiển '
                                '$%s$m về phía nam và $%s$ m về phía tây, đồng thời cách mặt đất $%s$ m$zz$ Chọn hệ trục tọa độ $Oxyz$ với gốc $O$ là vị trí người điều khiển, '
                                'mặt phẳng $(Oxy)$ trùng với mặt đất, trục $Ox$ có hướng trùng với hướng nam, trục $Oy$ có hướng trùng với hướng đông, trục $Oz$ vuông góc với mặt đất hướng lên bầu trời, '
                                'đơn vị trên mỗi trục tính theo mét$zz$ Khoảng cách giữa hai flycam đó bằng bao nhiêu mét (làm tròn kết quả đến hàng đơn vị)?'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb))
                                )

                # Nội dung lời giải
                loigiai = ('Vị trí $A,B$ có tọa độ lần lượt là: $(-%s;%s;%s),(%s;-%s;%s)$$zz$ Suy ra khoảng cách giữa hai flycam đó bằng:\\\\ \n'
                        '$$AB=\\sqrt{(%s-(-%s))^2+(-%s-%s)^2+(%s-%s)^2}\\approx %s \\text{(m)}$zz$$$'
                        %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),
                            latex(xb),latex(xa),latex(yb),latex(ya),latex(zb),latex(za),latex(kq)

                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

