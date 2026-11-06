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


def bt_dang5_p3_b3_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                a=randint(3,500)
                x0=Rational(a,2)
                x1=Rational(a,6)

                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                    'Xét đường tròn đường kính $AB=%s$ và một điểm $M$ di chuyển trên đoạn $AB$, đặt $AM=x$ ( Hình vẽ bên). Xét hai đường tròn đường kính $AM$ và $MB$. Kí hiệu $S(x)$'
                                ' là diện tích phần hình phẳng nằm trong hình tròn lớn và nằm ngoài hai hình tròn nhỏ. Các giá trị của $x$ để diện tích $S(x)$ không vượt quá một nửa tổng diện tích hai hình tròn nhỏ là '
                                '$\\hoac{&0<x<a \\\\ & b\\le x<%s }$. Khi đó $a+b$ bằng bao nhiêu?'
                                '}{'
                                '''\\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                \\clip(-0.6,-2.2) rectangle (5,2.5);
                \\draw [fill=black,pattern=north east lines,pattern color=black] (2.,0.) circle (2.cm);
                \\draw [color=ffffff,fill=ffffff,fill opacity=1.0] (0.8,0.) circle (0.8cm);
                \\draw [color=ffffff,fill=ffffff,fill opacity=1.0] (2.8,0.) circle (1.2cm);
                \\draw [dash pattern=on 2pt off 2pt] (1.6,0.)-- (1.6,2.2);
                \\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (0.,2.2);
                \\draw [->,dash pattern=on 1pt off 1pt] (1.6,2.2) -- (0.,2.2);
                \\draw [->,dash pattern=on 2pt off 2pt] (0.,2.2) -- (1.6,2.2);
                \\draw [->,dash pattern=on 1pt off 1pt] (0.,2.5909139798764835) -- (4.,2.6);
                \\draw [->,dash pattern=on 2pt off 2pt] (4.,2.6) -- (0.,2.5909139798764835);
                \\draw (-0.6,0.3) node[anchor=north west] {$A$};
                \\draw (4,0.3) node[anchor=north west] {$B$};
                \\draw (0.6325971134255984,2.550165790927442) node[anchor=north west] {$x$};
                \\draw (1.5,0.5) node[anchor=north west] {$M$};
                \\draw (0.6,1.4885213026002426) node[anchor=north west] {$S(x)$};
                \\draw(0.8,0.) circle (0.8cm);
                \\draw(2.8,0.) circle (1.2cm);
                \\draw (0.,0.)-- (4.,0.);
            \\end{tikzpicture}}'''
                                %(latex(a),latex(a))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có $S_{(O;AB)}=\\dfrac{AB^2}{4}\\pi;S_{(O_1;AM)}=\\dfrac{x^2}{4}\\pi; S_{(O_2;MB)}=\\dfrac{(%s-x)^2}{4}\\pi$ và $0<x<%s$.\\\\ \n'
                        'Khi đó $S(x)= S_{(O;AB)}-S_{(O_1;AM)}-S_{(O_2;MB)}=\\dfrac{\\pi}{4}\\left(AB^2-x^2-(%s-x)^2\\right)=\\dfrac{\\pi}{4}\\left(-2x^2+%sx\\right)$.\\\\ \n'
                        'Theo bài ta có $S(x)\\le\\dfrac{1}{2}\\left(S_{(O_1;AM)}+S_{(O_2;MB)}\\right) \\Rightarrow \\dfrac{\\pi }{4}\\left(-2x^2+%sx \\right)\\le \\dfrac{1}{2}\\cdot\\dfrac{\\pi }{4}\\left( x^2+(%s-x)^2 \\right)$\\\\ \n'
                        '$\\Rightarrow -6x^2+%sx-%s\\le0 \\Rightarrow \\hoac{&0<x \\le %s-%s\\sqrt{3} \\\\ & %s+%s\\sqrt{3}\\le x<%s }$.\\\\ \n'
                        'Khi đó $a=%s-%s\\sqrt{3},b=%s+%s\\sqrt{3}$.\\\\ \n'
                        'Vậy $a+b=\\left(%s-%s\\sqrt{3}\\right) +\\left(%s+%s\\sqrt{3}\\right) =%s$.'
                        %(latex(a),latex(a),
                            latex(a),latex(2*a),
                            latex(2*a),latex(a),
                            latex(6*a),latex(a**2),latex(x0),latex(x1),latex(x0),latex(x1), latex(a),latex(x0),latex(x1),latex(x0),latex(x1),
                            latex(x0),latex(x1),latex(x0),latex(x1),latex(a))
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

