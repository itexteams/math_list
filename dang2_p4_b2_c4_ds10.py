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


def bt_dang2_p4_b2_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                k=randint(1,3)
                a=4*k
                b=3*k
                c=1*k
                x0=Rational(b,c**2-c*a)
                y0=-Rational(a*b,c**2-c*a)
                x1=-Rational(y0,2*x0)
                y1=x0*x1**2+y0*x1


                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Tại một buổi khai trương của công ty, người ta làm một cổng chào có đường viền trong của mặt cắt là đường parabol. Khoảng cách giữa hai chân cổng là $%s$ m. Từ một điểm trên thân cổng người ta đo được khoảng cách tới mặt đất (điểm $H$) là $%s$ m và khoảng cách từ điểm H tới chân cổng gần nhất là $%s$ m. Hãy tính chiều cao của cổng chào đó (tính theo đường viền trong) theo đơn vị mét.'
                                '}{'
                                '''
                                \\definecolor{ffffff}{rgb}{1,1,1}
                                \\definecolor{qqwuqq}{rgb}{0,0.39215686274509803,0}
                                \\definecolor{ffzzqq}{rgb}{1,0.6,0}
                                \\definecolor{zzttqq}{rgb}{0.6,0.2,0}
                                \\definecolor{wwwwww}{rgb}{0.4,0.4,0.4}
                                \\definecolor{qqccqq}{rgb}{0,0.8,0}
                                \\definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1}
                                \\definecolor{cqcqcq}{rgb}{0.7529411764705882,0.7529411764705882,0.7529411764705882}
                                \\scalebox{0.6}{ 
                                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1cm,y=1cm]
                                \\clip(-4,-3) rectangle (4,5);
                                \\fill[line width=2pt,color=qqccqq,fill=qqccqq,fill opacity=1] (-3.1622776601683795,0) -- (3.162277660168379,0) -- (4,-1.2) -- (-4,-1.2) -- cycle;
                                \\draw[line width=0pt,color=ffzzqq,fill=ffzzqq,fill opacity=0.83] {[smooth,samples=50,domain=-3.1622776601683795:3.162277660168379] plot(\\x,{0})} -- (3.162277660168379,0) {[smooth,samples=50,domain=3.162277660168379:-3.1622776601683795] -- plot(\\x,{0-(3/6)*(\\x)^(2)+5})} -- (-3.1622776601683795,0) -- cycle;
                                \\draw[line width=0.8pt,color=ffffff,fill=ffffff,fill opacity=1] {[smooth,samples=50,domain=-2.8284271247461903:2.82842712474619] plot(\\x,{0})} -- (2.82842712474619,0) {[smooth,samples=50,domain=2.82842712474619:-2.8284271247461903] -- plot(\\x,{0-(1/2)*(\\x)^(2)+4})} -- (-2.8284271247461903,0) -- cycle;

                                \\draw [line width=2pt,color=qqccqq] (-3.1622776601683795,0)-- (3.162277660168379,0);
                                \\draw [line width=2pt,color=qqccqq] (3.162277660168379,0)-- (4,-1.2);
                                \\draw [line width=2pt,color=qqccqq] (4,-1.2)-- (-4,-1.2);
                                \\draw [line width=2pt,color=qqccqq] (-4,-1.2)-- (-3.1622776601683795,0);

                                \\draw[line width=1pt,color=zzttqq,smooth,samples=100,domain=-3.148:3.148] plot(\\x,{0-(3/6)*(\\x)^(2)+5});
                                \\draw[line width=1pt,color=qqwuqq,smooth,samples=100,domain=-2.812:2.812] plot(\\x,{0-(1/2)*(\\x)^(2)+4});
                                \\end{tikzpicture} }
                                '''
                                '}'
                                %(latex(a),latex(b),latex(c)
                                ))

                # Nội dung lời giải
                loigiai = (
                    '''
            \\begin{center}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.066310033285289,-0.9638335620855346) rectangle (5.021885972274304,5.017551987236173);
                    \\draw [samples=50,rotate around={-180.:(2.,4.)},xshift=2.cm,yshift=4.cm,line width=1.pt ,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                    \\draw [->,line width=1.pt ] (-1.,0.) -- (5.,0.);
                    \\draw [->,line width=1.pt ] (0.,-1.) -- (0.,5.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (1.,3.)-- (1.,0.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (1.,3.)-- (0.,3.);
                    \\draw (-0.6,0.49946968837352607) node[anchor=north west] {$O$};
                    \\draw (0.8,0.0722278634219755) node[anchor=north west] {$%s$};
                    \\draw (4,0.0722278634219755) node[anchor=north west] {$%s$};
                    \\draw (-0.40408520461038594,3.308584687429971) node[anchor=north west] {$%s$};
                    \\draw (1.027174908977308,0.49946968837352607) node[anchor=north west] {$H$};
                    \\draw (0.54,3.5542487367771125) node[anchor=north west] {$B$};
                    \\draw (4.594644147322754,-0.2) node[anchor=north west] {$x$};
                    \\draw (-0.5,5.006870941612385) node[anchor=north west] {$y$};
                \\end{tikzpicture}
            \\end{center}
                    '''
            'Chọn hệ trục tọa độ $(Oxy)$ sao cho gốc $O$ trùng với một chân của cổng, trục hoành nằm trêm đường nối hai chân cổng (đơn vị trên các trục tính theo mét) như hình vẽ. Gọi hàm số bậc hai có đồ thị chứa đường viền trong của cổng chào trên là $y=ax^2+bx+c$ với $a \\ne 0$. \\\\ \n'
            'Từ giả thiết bài toán ta có đồ thị hàm số đi qua các điểm $O(0;0), A(%s; 0), B(%s;%s)$. \\\\ \n'
            'Thay tọa độ các điểm trên vào hàm số, ta được $c=0$ và hệ phương trình \\\\ \n'
            '\\hspace*{1cm} $\\heva{&%s a+%s b=0 \\\\ & %s a+%s b=%s} \\Leftrightarrow \\heva{&a=%s \\\\ & b=%s.}$ \\\\ \n'
            'Suy ra ta có hàm số $y=%s x^2+%s x$. Từ đó đỉnh của đồ thị hàm số có tung độ là $%s$.\\\\ \n'
            'Vậy cổng chào có chiều cao $%s$ m.'
                        %(latex(c),latex(a),latex(b),
                            latex(a),latex(c),latex(b),
                            latex(a**2),latex(a),
                            latex(c**2),latex(c),latex(b),
                            latex(x0),latex(y0),
                            latex(x0),latex(y0),
                            latex(y1),
                            latex(y1)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('-1 x^2', '-x^2')
            return content

