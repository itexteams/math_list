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


def bt_dang20_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis1=[50,60,70,80,90,100,110,120,130,140,150]
                a=random.choice(lis1)
                b=a-40
                c=randint(1,2)
                lis2=[500000,550000,600000,650000,700000,750000]
                t=random.choice(lis2)
                x=symbols('x')
                f1=Rational(b,2)*sqrt(1-x**2/(Rational(a,2))**2)
                s1 = 2*integrate(f1, (x, -a/2, a/2))

                f2=Rational(b-2*c,2)*sqrt(1-x**2/(Rational(a-2*c,2))**2)
                s2 = 2*integrate(f2, (x, -(a-2*c)/2, (a-2*c)/2))

                h1=t*(s1-s2)/1000000
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Một sân chơi cho trẻ em hình chữ nhật có chiều dài $%s$ m và chiều rộng là $%s$ m người ta làm một con đường nằm trong sân (như hình vẽ). Biết rằng viền ngoài và viền trong của con đường là hai đường Elip, Elip của đường viền ngoài có trục lớn và trục bé lần lượt song song với các cạnh hình chữ nhật và chiều rộng của mặt đường là $%s$ m. Kinh phí cho mỗi m$^2$ làm đường $%s$ đồng. Tính số tiền (đơn vị: triệu) làm con đường đó (làm tròn kết quả đến hàng triệu).}
                                {
                                    \\scalebox{0.6}{ 
            \\begin{tikzpicture}
                \\fill[green] (-5,-3) rectangle (5,3);
                \\fill[white] (0,0) ellipse (5 and 3);
                \\fill[orange] (0,0) ellipse (4 and 2);
            \\end{tikzpicture} }}
            '''
                                %(latex(a),latex(b),latex(c),latex(t)
                                ))

                # Nội dung lời giải
                loigiai = ('''Xét hệ trục tọa độ $(Oxy)$ đặt gốc tọa độ $O$ vào tâm của hình Elip. \\\\
            Phương trình Elip của đường viền ngoài của con đường là $(E_1): \\frac{x^2}{%s^2} + \\frac{y^2}{%s^2} = 1$. \\\\
            Phần đồ thị của $(E_1)$ nằm phía trên trục hoành có phương trình $y = %s \\sqrt{1 - \\frac{x^2}{%s^2}} = f_1(x)$. \\\\
            Phương trình Elip của đường viền trong của con đường là $(E_2): \\frac{x^2}{%s^2} + \\frac{y^2}{%s^2} = 1$. \\\\
            Phần đồ thị của $(E_2)$ nằm phía trên trục hoành có phương trình $y = %s \\sqrt{1 - \\frac{x^2}{%s^2}} = f_2(x)$. \\\\
            Gọi $S_1$ là diện tích của $(E_1)$ và bằng hai lần diện tích phần hình phẳng giới hạn bởi trục hoành và đồ thị hàm số $y = f_1(x)$. Gọi $S_2$ là diện tích của $(E_2)$ và bằng hai lần diện tích phần hình phẳng giới hạn bởi trục hoành và đồ thị hàm số $y = f_2(x)$. \\\\
            Gọi $S$ là diện tích con đường. Khi đó \\\\
            $ S = S_1 - S_2 = 2\\int \\limits_{-%s}^{%s} %s \\sqrt{1 - \\frac{x^2}{%s^2}} \\text{d}x - 2\\int \\limits_{-%s}^{%s} %s \\sqrt{1 - \\frac{x^2}{%s^2}} \\text{d}x \\approx %s$.\\\\
            Vậy tổng số tiền làm con đường đó là $%s \\cdot S \\approx %s \\approx %s$ (triệu đồng).'''
                        %(latex(Rational(a,2)),latex(Rational(b,2)),
                            latex(Rational(b,2)),latex(Rational(a,2)),
                            latex(Rational(a-2*c,2)),latex(Rational(b-2*c,2)),
                            latex(Rational(b-2*c,2)),latex(Rational(a-2*c,2)),
                            latex(Rational(a,2)),latex(Rational(a,2)),
                            latex(Rational(b,2)),latex(Rational(a,2)),
                            latex(Rational(a-2*c,2)),latex(Rational(a-2*c,2)),
                            latex(Rational(b-2*c,2)),latex(Rational(a-2*c,2)),
                            latex(s1-s2),
                            latex(t),latex(t*(s1-s2)),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

