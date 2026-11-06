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


def bt_dang9_p3_b4_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x0=randint(16,21)
                y0=randint(16,21)
                z0=randint(16,21)
                a=symbols('a')
                f=2*a**2-2*(x0+y0+z0)*a+x0**2+y0**2+z0**2
                b=-(x0+y0+z0)
                c=x0**2+y0**2+z0**2
                delta=b**2-2*c
                while delta<=0:
                    x0=17
                    y0=18
                    z0=21
                    a=symbols('a')
                    f=2*a**2-2*(x0+y0+z0)*a+x0**2+y0**2+z0**2
                    b=-(x0+y0+z0)
                    c=x0**2+y0**2+z0**2
                    delta=b**2-2*c
                x1=(-b+sqrt(delta))/2
                x2=(-b-sqrt(delta))/2
                m=round(x2-0.5,1)
                n=round(x2+0.5,1)
                h1=2*x2  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Một quả bóng rổ được đặt ở một góc của căn phòng hình hộp chữ nhật, sao cho quả bóng chạm và tiếp xúc với hai bức tường và nền nhà của căn phòng đó thì có một điểm trên quả bóng có khoảng cách lần lượt đến hai bức tường và nền nhà là $%s$ cm, $%s$ cm, $%s$ cmzz Hỏi độ dài đương kính của quả bóng bằng bao nhiêu cm biết rằng quả bóng rổ tiêu chuẩn có bán kính từ $%s$ cm đến $%s$ cm? (Kết quả là tròn đến hàng thập phân)zz}
                                {\\definecolor{ffxfqq}{rgb}{1zz,0zz4980392156862745,0zz}
            \\definecolor{ffffzz}{rgb}{1zz,1zz,0zz6}
            \\definecolor{ffffff}{rgb}{1zz,1zz,1zz}
            \\definecolor{zzccff}{rgb}{0zz6,0zz8,1zz}
            \\definecolor{afeeee}{rgb}{0zz6862745098039216,0zz9333333333333333,0zz9333333333333333}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-0zz0882037939997747,-0zz04375873443539242) rectangle (5zz067203352028975,3zz819039039702758);
                    \\fill[line width=0zzpt,color=afeeee,fill=afeeee,fill opacity=1zz0] (0zz,1zz1664461822649859) -- (2zz2940843499959187,1zz595446942394185) -- (2zz2634414385581185,3zz7710936544779807) -- (0zz,3zz7710936544779807) -- cycle;
                    \\fill[line width=0zzpt,color=zzccff,fill=zzccff,fill opacity=1zz0] (2zz2940843499959187,1zz595446942394185) -- (4zz978403391947199,0zz8293741564491864) -- (4zz984531974234759,3zz795607983628221) -- (2zz2634414385581185,3zz7710936544779807) -- cycle;
                    \\fill[line width=0zzpt,color=ffffff,fill=ffffff,fill opacity=1zz0] (0zz,1zz1664461822649859) -- (0zz,0zz8355027387367465) -- (2zz2940843499959187,1zz3319179040291056) -- (2zz2940843499959187,1zz595446942394185) -- cycle;
                    \\fill[line width=0zzpt,color=ffffff,fill=ffffff,fill opacity=1zz0] (2zz2940843499959187,1zz3319179040291056) -- (4zz984645000151492,0zz4647919830376981) -- (4zz978403391947199,0zz8293741564491864) -- (2zz2940843499959187,1zz595446942394185) -- cycle;
                    \\fill[line width=0zzpt,color=ffffzz,fill=ffffzz,fill opacity=1zz0] (0zz,0zz) -- (0zz,0zz8355027387367465) -- (2zz2940843499959187,1zz3319179040291056) -- (4zz984645000151492,0zz4647919830376981) -- (5zz,0zz) -- cycle;
                    \\draw [line width=1zzpt,color=ffxfqq,fill=ffxfqq,fill opacity=1zz0] (2zz6035187414491547,1zz8979107853000352) circle (1zz3780280584523876cm);
                    \\draw [shift={(2zz9625504873920003,1zz7428363735274706)},line width=1zzpt]  plot[domain=1zz4561838191843608:4zz011560184084384,variable=\\t]({1zz*1zz4391867363774549*cos(\\t r)+0zz*1zz4391867363774549*sin(\\t r)},{0zz*1zz4391867363774549*cos(\\t r)+1zz*1zz4391867363774549*sin(\\t r)});
                    \\draw [shift={(1zz9181602299007048,2zz665738777811168)},line width=1zzpt]  plot[domain=2zz7210713237445514:4zz955586284333985,variable=\\t]({1zz*0zz3729944702110082*cos(\\t r)+0zz*0zz3729944702110082*sin(\\t r)},{0zz*0zz3729944702110082*cos(\\t r)+1zz*0zz3729944702110082*sin(\\t r)});
                    \\draw [shift={(4zz9627511918538385,-16zz465952482532323)},line width=1zzpt]  plot[domain=1zz6882970193581803:1zz7269375463733436,variable=\\t]({1zz*19zz00082350429537*cos(\\t r)+0zz*19zz00082350429537*sin(\\t r)},{0zz*19zz00082350429537*cos(\\t r)+1zz*19zz00082350429537*sin(\\t r)});
                    \\draw [shift={(2zz978585915573923,1zz042733238767557)},line width=1zzpt]  plot[domain=0zz7630770953092151:1zz7476855209752908,variable=\\t]({1zz*1zz382697832955611*cos(\\t r)+0zz*1zz382697832955611*sin(\\t r)},{0zz*1zz382697832955611*cos(\\t r)+1zz*1zz382697832955611*sin(\\t r)});
                    \\draw [shift={(3zz680372607547036,4zz513091639017344)},line width=1zzpt]  plot[domain=3zz8925293417892783:4zz751024925176731,variable=\\t]({1zz*3zz288208865080329*cos(\\t r)+0zz*3zz288208865080329*sin(\\t r)},{0zz*3zz288208865080329*cos(\\t r)+1zz*3zz288208865080329*sin(\\t r)});
                    \\draw [shift={(1zz3193811969630858,1zz3945135977430407)},line width=1zzpt]  plot[domain=0zz4237232942480808:1zz7988805980713085,variable=\\t]({1zz*0zz3911656452897418*cos(\\t r)+0zz*0zz3911656452897418*sin(\\t r)},{0zz*0zz3911656452897418*cos(\\t r)+1zz*0zz3911656452897418*sin(\\t r)});
                    \\draw [shift={(8zz270278001240838,6zz2597604156444815)},line width=1zzpt]  plot[domain=3zz761257956850915:3zz8479636499779715,variable=\\t]({1zz*8zz100410018770827*cos(\\t r)+0zz*8zz100410018770827*sin(\\t r)},{0zz*8zz100410018770827*cos(\\t r)+1zz*8zz100410018770827*sin(\\t r)});
                    \\draw [shift={(3zz220576525540542,2zz252097050894002)},line width=1zzpt]  plot[domain=3zz985194856823764:4zz600997921768578,variable=\\t]({1zz*1zz6734381261923847*cos(\\t r)+0zz*1zz6734381261923847*sin(\\t r)},{0zz*1zz6734381261923847*cos(\\t r)+1zz*1zz6734381261923847*sin(\\t r)});
            \\end{tikzpicture}}'''
                                %(latex(x0),latex(y0),latex(z0),latex(m),latex(n)
                                ))

                # Nội dung lời giải
                loigiai = ('''Ta đặt hệ trục vào căn phòng sao cho có hai bức tường là mặt $(Oxz)$, $(Oyz)$, và nền là $(Oxy)$zz \\\\
            Vậy bài toán dẫn đến việc tìm đường kính của mặt cầu tiếp xúc với 3 mặt phẳng tọa độ và chứa điểm $M(%s; %s; %s)$zz\\\\
            Ta có thể gọi phương trình mặt cầu là $(S): (x-a)^2 + (y-a)^2 + (z-a)^2 = a^2$, với $a > 0$ (do mặt cầu tiếp xúc với các mặt phẳng tọa độ nên $a = b = c = R$)zz\\\\
            Do $M(%s; %s; %s) \\in (S)$ nên $(%s-a)^2 + (%s-a)^2 + (%s-a)^2 = a^2$zz\\\\
            $\\Rightarrow %s = 0 \\Leftrightarrow \\hoac{ & a = %s \\\\& a = %s }$\\\\
            Vì quả bóng rổ tiêu chuẩn có đường kính từ $%s$ cm đến $%s$ cm nên $a = %s$ thỏa mãnzz\\\\
            Vậy đường kính quả bóng bằng $2a = 2\\left(%s\\right) \\approx %s$ cmzz\\\\'''
                        %(latex(x0),latex(y0),latex(z0),
                            latex(x0),latex(y0),latex(z0),
                            latex(x0),latex(y0),latex(z0),
                            latex(f),latex(x1),latex(x2),
                            latex(m),latex(n),latex(x2),
                            latex(x2),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content

